#!/usr/bin/env python3
import json
from pathlib import Path

SEED = Path(__file__).parents[1] / "ontology" / "seed.json"

def consonance(a):
    # Toy mapping: value near 1 → consonant, near 0 → dissonant
    x = a.get('default', 0.5)
    return round(1 - abs(0.5 - x)*2, 3)

def main():
    data = json.loads(SEED.read_text())
    axes = data.get('axes', [])
    total = sum(consonance(ax) for ax in axes)
    score = round(total / max(1, len(axes)), 3)
    print({
        'axes': axes,
        'coherenceScore': score,
        'explanation': 'Toy metric: average proximity to midpoint as neutrality → refine per spec.'
    })

if __name__ == '__main__':
    main()