#!/usr/bin/env python3
"""
Integration test: Graph API <-> Federation Python server

Steps:
1) Start Graph API (uvicorn prototypes.graph.api:app on :8000)
2) Start Federation server (python prototypes/federation-python/fractal_server.py on :8788) with GRAPH_API_URL env
3) Poll readiness, then validate ontology data is accessible and aligned:
   - /nodes and /nodes/{id} on Graph API expose chakra/colorHex/baseFrequencyHz/planet
   - /fractal/nodes/{id} on Federation includes chakra/color_hex/base_frequency_hz/planet
   - Compare Graph API values (camelCase) with Federation values (snake_case)
4) Print concise PASS/FAIL summary, exit non-zero on failure
"""

import os
import sys
import time
import signal
import subprocess
import shutil
from typing import Dict, Any

try:
    import requests
except Exception:
    print("ERROR: Python 'requests' package is required. Try: python -m pip install requests", file=sys.stderr)
    sys.exit(2)


GRAPH_URL = os.getenv("GRAPH_API_URL", "http://127.0.0.1:8000")
FED_URL = os.getenv("FED_URL", "http://127.0.0.1:8788")


def wait_for(url: str, timeout_s: int = 30) -> bool:
    start = time.time()
    while time.time() - start < timeout_s:
        try:
            r = requests.get(url, timeout=2)
            if r.ok:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


class ManagedProcess:
    def __init__(self, popen: subprocess.Popen):
        self.popen = popen

    def stop(self):
        if self.popen.poll() is not None:
            return
        try:
            if os.name == 'nt':
                self.popen.terminate()
            else:
                self.popen.send_signal(signal.SIGTERM)
            self.popen.wait(timeout=8)
        except Exception:
            try:
                self.popen.kill()
            except Exception:
                pass


def start_graph_api() -> ManagedProcess:
    # Prefer running uvicorn module if available
    cmd = [sys.executable, "-m", "uvicorn", "prototypes.graph.api:app", "--host", "127.0.0.1", "--port", "8000"]
    env = os.environ.copy()
    p = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return ManagedProcess(p)


def start_federation(graph_url: str) -> ManagedProcess:
    env = os.environ.copy()
    env["GRAPH_API_URL"] = graph_url
    cmd = [sys.executable, "prototypes/federation-python/fractal_server.py"]
    p = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return ManagedProcess(p)


def free_port(port: int):
    if os.name == 'nt':
        # Use PowerShell to find and kill process holding the port
        ps = (
            f"$c=Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue; "
            f"if($c){{ try{{ Stop-Process -Id $($c.OwningProcess) -Force }} catch {{}} }}"
        )
        try:
            subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass
    else:
        # Best-effort on *nix
        try:
            subprocess.run(["bash", "-lc", f"fuser -k {port}/tcp"], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass


def get_graph_node(node_id: str) -> Dict[str, Any]:
    r = requests.get(f"{GRAPH_URL}/nodes/{node_id}", timeout=5)
    r.raise_for_status()
    return r.json()


def get_fed_node(node_id: str) -> Dict[str, Any]:
    r = requests.get(f"{FED_URL}/fractal/nodes/{node_id}", timeout=5)
    r.raise_for_status()
    return r.json()


def main() -> int:
    free_port(8000)
    print("Starting Graph API on http://127.0.0.1:8000 ...")
    graph = start_graph_api()
    if not wait_for(f"{GRAPH_URL}/nodes"):
        graph.stop()
        print("FAIL: Graph API did not start within timeout", file=sys.stderr)
        return 1
    print("Graph API is up.")

    # Ensure a clean fractal storage so bootstrap reflects current ontology
    storage_dir = os.path.join(os.getcwd(), "fractal-storage")
    if os.path.isdir(storage_dir):
        print("Removing existing fractal-storage directory for a clean bootstrap ...")
        shutil.rmtree(storage_dir, ignore_errors=True)

    free_port(8788)
    print("Starting Federation server on http://127.0.0.1:8788 ...")
    fed = start_federation(GRAPH_URL)
    if not wait_for(f"{FED_URL}/fractal/levels"):
        fed.stop(); graph.stop()
        print("FAIL: Federation server did not start within timeout", file=sys.stderr)
        return 1
    print("Federation server is up.")

    try:
        # Validate Graph API basic queries
        print("Validating Graph API nodes endpoint ...")
        r = requests.get(f"{GRAPH_URL}/nodes?ids=codex:Void,codex:Flow", timeout=5)
        r.raise_for_status()
        nodes = {n.get("id"): n for n in r.json()}
        assert "codex:Void" in nodes and "codex:Flow" in nodes, "Missing expected core nodes from Graph API"
        for nid in ["codex:Void", "codex:Flow"]:
            n = nodes[nid]
            for k in ["chakra", "colorHex", "baseFrequencyHz", "planet"]:
                assert k in n, f"Graph API node {nid} missing field {k}"

        # Validate single node and Federation mapping alignment
        print("Validating Federation aligns with Graph API meta ...")
        g_void = get_graph_node("codex:Void")
        f_void = get_fed_node("codex:Void")

        # Compare fields (camelCase vs snake_case)
        mapping = {
            "chakra": "chakra",
            "colorHex": "color_hex",
            "baseFrequencyHz": "base_frequency_hz",
            "planet": "planet",
        }
        for gk, fk in mapping.items():
            gv = g_void.get(gk)
            fv = f_void.get(fk)
            assert gv == fv, f"Mismatch for {gk}/{fk}: Graph={gv} Federation={fv}"

        # Validate federation levels & a subnode expansion path
        r = requests.get(f"{FED_URL}/fractal/levels", timeout=5)
        r.raise_for_status()
        levels = r.json()
        assert 1 in levels.get("fractal_levels", []) and 2 in levels.get("fractal_levels", []), "Federation fractal levels missing"

        r = requests.get(f"{FED_URL}/fractal/subnodes/codex:Void", timeout=5)
        if r.ok:
            subs = r.json()
            assert "subnodes" in subs, "Federation missing subnodes grouping"

        print("PASS: Integration validated successfully.")
        return 0
    except Exception as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 1
    finally:
        fed.stop()
        graph.stop()


if __name__ == "__main__":
    sys.exit(main())


