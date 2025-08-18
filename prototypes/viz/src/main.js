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

// Simple Flower of Life points
function flowerPoints(radius=3, rings=2){
  const pts=[new THREE.Vector3(0,0,0)];
  for(let r=1;r<=rings;r++){
    const n=6*r; const ang=2*Math.PI/n; const R=r*radius;
    for(let i=0;i<n;i++) pts.push(new THREE.Vector3(Math.cos(i*ang)*R, Math.sin(i*ang)*R, 0));
  }
  return pts;
}

const nodes = [
  { id: 'codex:Void', waterState:'Plasma' },
  { id: 'codex:Field', waterState:'Vapor' },
  { id: 'codex:Pattern', waterState:'Structured' },
  { id: 'codex:Flow', waterState:'Liquid' },
  { id: 'codex:Memory', waterState:'Ice' },
  { id: 'codex:Resonance', waterState:'Clustered' },
  { id: 'codex:Transformation', waterState:'Supercritical' },
  { id: 'codex:Unity', waterState:'LiquidCrystalBoundary' },
  { id: 'codex:Emergence', waterState:'VaporLiquidEquilibrium' },
  { id: 'codex:Awareness', waterState:'ReflectiveSurface' },
  { id: 'codex:Node', waterState:'SteamSpark' },
  { id: 'codex:Codex', waterState:'AllStates' }
];

const pts = flowerPoints(3, 2);
const geo = new THREE.SphereGeometry(0.35, 24, 24);

nodes.forEach((n,i)=>{
  const color = palette[n.waterState] || 0xffffff;
  const mat = new THREE.MeshStandardMaterial({ color, emissive: color, emissiveIntensity: 0.25, metalness: 0.1, roughness: 0.4 });
  const m = new THREE.Mesh(geo, mat);
  const p = pts[i % pts.length];
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