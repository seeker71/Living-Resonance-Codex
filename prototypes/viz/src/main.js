import * as THREE from 'three';

const app = document.getElementById('app');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, innerWidth/innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setSize(innerWidth, innerHeight); app.appendChild(renderer.domElement);

camera.position.z = 24;

// Water-state palette
const palette = {
  Ice: 0x6db7ff,
  Liquid: 0xaee0ff,
  Vapor: 0xffd480,
  Plasma: 0xff7a7a,
  Structured: 0x9cd1ff,
  Clustered: 0xc9a0ff,
  Supercritical: 0xff9db5,
  ReflectiveSurface: 0xbfe8ff,
  LiquidCrystalBoundary: 0xd1ffe6,
  VaporLiquidEquilibrium: 0xfff2cc,
  SteamSpark: 0xffc2b3,
  AllStates: 0xffffff
};

// Enhanced Flower of Life points with proper positioning
function flowerPoints(radius=3, rings=2){
  const pts=[new THREE.Vector3(0,0,0)];
  for(let r=1;r<=rings;r++){
    const n=6*r; const ang=2*Math.PI/n; const R=r*radius;
    for(let i=0;i<n;i++) pts.push(new THREE.Vector3(Math.cos(i*ang)*R, Math.sin(i*ang)*R, 0));
  }
  return pts;
}

// Get position from node geometry or fallback to flower pattern
function getNodePosition(node, index, pts) {
  if (node.geometry && node.geometry.position) {
    return new THREE.Vector3(node.geometry.position[0], node.geometry.position[1], 0);
  }
  return pts[index % pts.length];
}

const nodes = [
  { id: 'codex:Void', waterState:'Plasma', geometry: { position: [0, 0], scale: 1.0 } },
  { id: 'codex:Field', waterState:'Vapor', geometry: { position: [0, 3], scale: 0.8 } },
  { id: 'codex:Pattern', waterState:'Structured', geometry: { position: [2.6, 1.5], scale: 0.8 } },
  { id: 'codex:Flow', waterState:'Liquid', geometry: { position: [2.6, -1.5], scale: 0.8 } },
  { id: 'codex:Memory', waterState:'Ice', geometry: { position: [0, -3], scale: 0.8 } },
  { id: 'codex:Resonance', waterState:'Clustered', geometry: { position: [-2.6, -1.5], scale: 0.8 } },
  { id: 'codex:Transformation', waterState:'Supercritical', geometry: { position: [-2.6, 1.5], scale: 0.8 } },
  { id: 'codex:Unity', waterState:'LiquidCrystalBoundary', geometry: { position: [1.5, 2.6], scale: 0.6 } },
  { id: 'codex:Emergence', waterState:'VaporLiquidEquilibrium', geometry: { position: [3, 0], scale: 0.6 } },
  { id: 'codex:Awareness', waterState:'ReflectiveSurface', geometry: { position: [1.5, -2.6], scale: 0.6 } },
  { id: 'codex:Node', waterState:'SteamSpark', geometry: { position: [-1.5, -2.6], scale: 0.6 } },
  { id: 'codex:Codex', waterState:'AllStates', geometry: { position: [-3, 0], scale: 0.6 } }
];

const pts = flowerPoints(3, 2);
const geo = new THREE.SphereGeometry(0.35, 24, 24);

nodes.forEach((n,i)=>{
  const color = palette[n.waterState] || 0xffffff;
  const scale = n.geometry?.scale || 1.0;
  const geo = new THREE.SphereGeometry(0.35 * scale, 24, 24);
  const mat = new THREE.MeshStandardMaterial({ color, emissive: color, emissiveIntensity: 0.25, metalness: 0.1, roughness: 0.4 });
  const m = new THREE.Mesh(geo, mat);
  const p = getNodePosition(n, i, pts);
  m.position.set(p.x, p.y, p.z);
  m.userData = n;
  scene.add(m);
});

const light = new THREE.PointLight(0xffffff, 2, 200); light.position.set(0,0,16); scene.add(light);
const amb = new THREE.AmbientLight(0x446677, 0.5); scene.add(amb);

function animate(){
  requestAnimationFrame(animate);
  scene.rotation.z += 0.0015;
  renderer.render(scene, camera);
}

addEventListener('resize', ()=>{camera.aspect=innerWidth/innerHeight; camera.updateProjectionMatrix(); renderer.setSize(innerWidth, innerHeight)});
animate();