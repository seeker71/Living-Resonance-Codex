import * as THREE from 'three';

// Resonance-driven visualization system
class LivingCodexViz {
  constructor() {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(60, innerWidth/innerHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
    this.clock = new THREE.Clock();
    
    this.nodes = [];
    this.edges = [];
    this.geometries = {};
    this.resonanceState = {
      currentAxis: 'Fear-Trust',
      axisValue: 0.5,
      resonanceAmplitude: 1.0
    };
    
    this.init();
  }
  
  init() {
    // Setup renderer
    this.renderer.setSize(innerWidth, innerHeight);
    this.renderer.setClearColor(0x0a0a0a, 0.9);
    document.getElementById('app').appendChild(this.renderer.domElement);
    
    // Setup camera
    this.camera.position.z = 24;
    
    // Setup lighting
    this.setupLighting();
    
    // Load sacred geometries
    this.createSacredGeometries();
    
    // Create nodes
    this.createNodes();
    
    // Create edges
    this.createEdges();
    
    // Setup controls
    this.setupControls();
    
    // Start animation
    this.animate();
    
    // Handle resize
    window.addEventListener('resize', () => this.onWindowResize());
  }
  
  setupLighting() {
    // Main light
    const mainLight = new THREE.PointLight(0xffffff, 2, 200);
    mainLight.position.set(0, 0, 16);
    this.scene.add(mainLight);
    
    // Ambient light
    const ambientLight = new THREE.AmbientLight(0x446677, 0.5);
    this.scene.add(ambientLight);
    
    // Resonance light (follows mouse)
    this.resonanceLight = new THREE.PointLight(0x00ffff, 1, 50);
    this.resonanceLight.position.set(0, 0, 10);
    this.scene.add(this.resonanceLight);
  }
  
  createSacredGeometries() {
    // Flower of Life
    this.geometries.flowerOfLife = this.createFlowerOfLife();
    
    // Icositetragon Wheel (24-point mandala)
    this.geometries.icositetragon = this.createIcositetragon();
    
    // Metatron's Cube
    this.geometries.metatronCube = this.createMetatronCube();
    
    // Add to scene
    this.scene.add(this.geometries.flowerOfLife);
    this.scene.add(this.geometries.icositetragon);
    this.scene.add(this.geometries.metatronCube);
  }
  
  createFlowerOfLife() {
    const group = new THREE.Group();
    const radius = 3;
    const rings = 2;
    
    // Create overlapping circles using flowerPoints positioning
    const flowerPoints = this.flowerPoints(radius, rings);
    
    for (let r = 1; r <= rings; r++) {
      const n = 6 * r;
      const ang = 2 * Math.PI / n;
      const R = r * radius;
      
      for (let i = 0; i < n; i++) {
        const circle = new THREE.Mesh(
          new THREE.RingGeometry(R - 0.1, R + 0.1, 32),
          new THREE.MeshBasicMaterial({ 
            color: 0x444444, 
            transparent: true, 
            opacity: 0.3 
          })
        );
        circle.position.set(
          Math.cos(i * ang) * R,
          Math.sin(i * ang) * R,
          0
        );
        group.add(circle);
      }
    }
    
    return group;
  }
  
  // Enhanced Flower of Life points with proper positioning
  flowerPoints(radius=3, rings=2) {
    const pts = [new THREE.Vector3(0, 0, 0)];
    for (let r = 1; r <= rings; r++) {
      const n = 6 * r;
      const ang = 2 * Math.PI / n;
      const R = r * radius;
      for (let i = 0; i < n; i++) {
        pts.push(new THREE.Vector3(Math.cos(i * ang) * R, Math.sin(i * ang) * R, 0));
      }
    }
    return pts;
  }
  
  createIcositetragon() {
    const group = new THREE.Group();
    const radius = 8;
    const points = 24;
    
    // Create 24-point mandala
    for (let i = 0; i < points; i++) {
      const angle = (i / points) * 2 * Math.PI;
      const x = Math.cos(angle) * radius;
      const y = Math.sin(angle) * radius;
      
      // Point marker
      const point = new THREE.Mesh(
        new THREE.SphereGeometry(0.1, 8, 8),
        new THREE.MeshBasicMaterial({ 
          color: 0x666666, 
          transparent: true, 
          opacity: 0.5 
        })
      );
      point.position.set(x, y, 0);
      group.add(point);
      
      // Connection lines
      if (i > 0) {
        const prevAngle = ((i - 1) / points) * 2 * Math.PI;
        const prevX = Math.cos(prevAngle) * radius;
        const prevY = Math.sin(prevAngle) * radius;
        
        const line = new THREE.Line(
          new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(prevX, prevY, 0),
            new THREE.Vector3(x, y, 0)
          ]),
          new THREE.LineBasicMaterial({ 
            color: 0x444444, 
            transparent: true, 
            opacity: 0.2 
          })
        );
        group.add(line);
      }
    }
    
    // Connect last to first
    const lastLine = new THREE.Line(
      new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(
          Math.cos(((points - 1) / points) * 2 * Math.PI) * radius,
          Math.sin(((points - 1) / points) * 2 * Math.PI) * radius,
          0
        ),
        new THREE.Vector3(radius, 0, 0)
      ]),
      new THREE.LineBasicMaterial({ 
        color: 0x444444, 
        transparent: true, 
        opacity: 0.2 
      })
    );
    group.add(lastLine);
    
    return group;
  }
  
  createMetatronCube() {
    const group = new THREE.Group();
    const radius = 12;
    
    // Create outer sphere
    const outerSphere = new THREE.Mesh(
      new THREE.SphereGeometry(radius, 32, 32),
      new THREE.MeshBasicMaterial({ 
        color: 0x333333, 
        transparent: true, 
        opacity: 0.1,
        wireframe: true
      })
    );
    group.add(outerSphere);
    
    // Create inner spheres at sacred geometry points
    const sacredPoints = [
      [0, 0], [0, radius/2], [radius/2, 0], [-radius/2, 0], [0, -radius/2],
      [radius/2, radius/2], [-radius/2, radius/2], [radius/2, -radius/2], [-radius/2, -radius/2]
    ];
    
    sacredPoints.forEach(([x, y]) => {
      const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(0.3, 16, 16),
        new THREE.MeshBasicMaterial({ 
          color: 0x555555, 
          transparent: true, 
          opacity: 0.4 
        })
      );
      sphere.position.set(x, y, 0);
      group.add(sphere);
    });
    
    return group;
  }
  
  createNodes() {
    // Water-state palette with resonance enhancement
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
    
    const nodeData = [
      { id: 'codex:Void', waterState: 'Plasma', geometry: { position: [0, 0], scale: 1.0 }, resonance: 1.0 },
      { id: 'codex:Field', waterState: 'Vapor', geometry: { position: [0, 3], scale: 0.8 }, resonance: 0.8 },
      { id: 'codex:Pattern', waterState: 'Structured', geometry: { position: [2.6, 1.5], scale: 0.8 }, resonance: 0.9 },
      { id: 'codex:Flow', waterState: 'Liquid', geometry: { position: [2.6, -1.5], scale: 0.8 }, resonance: 0.7 },
      { id: 'codex:Memory', waterState: 'Ice', geometry: { position: [0, -3], scale: 0.8 }, resonance: 0.6 },
      { id: 'codex:Resonance', waterState: 'Clustered', geometry: { position: [-2.6, -1.5], scale: 0.8 }, resonance: 0.9 },
      { id: 'codex:Transformation', waterState: 'Supercritical', geometry: { position: [-2.6, 1.5], scale: 0.8 }, resonance: 0.8 },
      { id: 'codex:Unity', waterState: 'LiquidCrystalBoundary', geometry: { position: [1.5, 2.6], scale: 0.6 }, resonance: 0.7 },
      { id: 'codex:Emergence', waterState: 'VaporLiquidEquilibrium', geometry: { position: [3, 0], scale: 0.6 }, resonance: 0.6 },
      { id: 'codex:Awareness', waterState: 'ReflectiveSurface', geometry: { position: [1.5, -2.6], scale: 0.6 }, resonance: 0.8 },
      { id: 'codex:Node', waterState: 'SteamSpark', geometry: { position: [-1.5, -2.6], scale: 0.6 }, resonance: 0.7 },
      { id: 'codex:Codex', waterState: 'AllStates', geometry: { position: [-3, 0], scale: 0.6 }, resonance: 1.0 }
    ];
    
    nodeData.forEach((nodeData, i) => {
      const node = this.createNode(nodeData, palette);
      this.nodes.push(node);
      this.scene.add(node);
    });
  }
  
  createNode(nodeData, palette) {
    const color = palette[nodeData.waterState] || 0xffffff;
    const scale = nodeData.geometry.scale;
    const resonance = nodeData.resonance;
    
    // Create node geometry
    const geometry = new THREE.SphereGeometry(0.35 * scale, 24, 24);
    const material = new THREE.MeshStandardMaterial({ 
      color: color, 
      emissive: color, 
      emissiveIntensity: 0.25 * resonance, 
      metalness: 0.1, 
      roughness: 0.4 
    });
    
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(
      nodeData.geometry.position[0],
      nodeData.geometry.position[1],
      0
    );
    
    // Store node data
    mesh.userData = {
      ...nodeData,
      originalColor: color,
      currentResonance: resonance
    };
    
    // Add resonance glow
    const glowGeometry = new THREE.SphereGeometry(0.4 * scale, 16, 16);
    const glowMaterial = new THREE.MeshBasicMaterial({
      color: color,
      transparent: true,
      opacity: 0.3 * resonance
    });
    
    const glow = new THREE.Mesh(glowGeometry, glowMaterial);
    mesh.add(glow);
    
    return mesh;
  }
  
  createEdges() {
    // Create edges between related nodes
    const edgeData = [
      { from: 'codex:Void', to: 'codex:Field' },
      { from: 'codex:Void', to: 'codex:Pattern' },
      { from: 'codex:Field', to: 'codex:Pattern' },
      { from: 'codex:Pattern', to: 'codex:Flow' },
      { from: 'codex:Flow', to: 'codex:Memory' },
      { from: 'codex:Memory', to: 'codex:Resonance' },
      { from: 'codex:Resonance', to: 'codex:Transformation' },
      { from: 'codex:Transformation', to: 'codex:Unity' },
      { from: 'codex:Unity', to: 'codex:Emergence' },
      { from: 'codex:Emergence', to: 'codex:Awareness' },
      { from: 'codex:Awareness', to: 'codex:Node' },
      { from: 'codex:Node', to: 'codex:Codex' }
    ];
    
    edgeData.forEach(edgeData => {
      const edge = this.createEdge(edgeData);
      if (edge) {
        this.edges.push(edge);
        this.scene.add(edge);
      }
    });
  }
  
  createEdge(edgeData) {
    const fromNode = this.nodes.find(n => n.userData.id === edgeData.from);
    const toNode = this.nodes.find(n => n.userData.id === edgeData.to);
    
    if (!fromNode || !toNode) return null;
    
    const geometry = new THREE.BufferGeometry().setFromPoints([
      fromNode.position,
      toNode.position
    ]);
    
    const material = new THREE.LineBasicMaterial({
      color: 0x666666,
      transparent: true,
      opacity: 0.4
    });
    
    const line = new THREE.Line(geometry, material);
    line.userData = edgeData;
    
    return line;
  }
  
  setupControls() {
    // Mouse interaction
    document.addEventListener('mousemove', (event) => {
      const mouse = new THREE.Vector2();
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
      
      // Update resonance light position
      this.resonanceLight.position.x = mouse.x * 20;
      this.resonanceLight.position.y = mouse.y * 20;
      
      // Create attention waves
      this.createAttentionWave(mouse.x * 20, mouse.y * 20);
    });
    
    // Click interaction
    document.addEventListener('click', (event) => {
      const mouse = new THREE.Vector2();
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
      
      this.handleNodeClick(mouse);
    });
    
    // Setup interactive sliders
    this.setupSliders();
    
    // Setup control buttons
    this.setupControlButtons();
  }
  
  setupSliders() {
    const sliders = document.querySelectorAll('.slider-container');
    
    sliders.forEach(slider => {
      const track = slider.querySelector('.slider-track');
      const thumb = slider.querySelector('.slider-thumb');
      const valueDisplay = slider.parentElement.querySelector('.axis-value');
      const axis = slider.dataset.axis;
      
      let isDragging = false;
      
      const updateSlider = (clientX) => {
        const rect = slider.getBoundingClientRect();
        const x = clientX - rect.left;
        const percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));
        
        track.style.width = percentage + '%';
        thumb.style.left = percentage + '%';
        
        const value = (percentage / 100).toFixed(2);
        valueDisplay.textContent = value;
        
        // Update resonance state
        this.updateResonance(axis, parseFloat(value));
      };
      
      slider.addEventListener('mousedown', (e) => {
        isDragging = true;
        updateSlider(e.clientX);
      });
      
      document.addEventListener('mousemove', (e) => {
        if (isDragging) {
          updateSlider(e.clientX);
        }
      });
      
      document.addEventListener('mouseup', () => {
        isDragging = false;
      });
      
      // Click to set value
      slider.addEventListener('click', (e) => {
        updateSlider(e.clientX);
      });
    });
  }
  
  setupControlButtons() {
    // Toggle geometry visibility
    document.getElementById('toggle-geometry').addEventListener('click', () => {
      Object.values(this.geometries).forEach(geometry => {
        geometry.visible = !geometry.visible;
      });
    });
    
    // Reset resonance to balanced state
    document.getElementById('reset-resonance').addEventListener('click', () => {
      this.resetResonance();
    });
    
    // Show fractal level info
    document.getElementById('fractal-zoom').addEventListener('click', () => {
      document.getElementById('fractal-level').classList.add('show');
    });
    
    // Close fractal level
    document.getElementById('close-fractal').addEventListener('click', () => {
      document.getElementById('fractal-level').classList.remove('show');
    });
    
    // Water cycle animation
    document.getElementById('water-cycle').addEventListener('click', () => {
      this.animateWaterCycle();
    });
  }
  
  updateResonance(axis, value) {
    // Update resonance state
    this.resonanceState[axis] = value;
    
    // Calculate overall coherence
    const axes = ['fear-trust', 'pattern-flow', 'ownership-stewardship', 'protection-openness', 'noise-harmony'];
    const values = axes.map(ax => this.resonanceState[ax] || 0.5);
    const coherence = values.reduce((sum, val) => sum + (1 - Math.abs(0.5 - val) * 2), 0) / values.length;
    
    // Update display
    document.getElementById('coherence-score').textContent = coherence.toFixed(2);
    
    // Update water state based on coherence
    const waterState = this.getWaterStateFromCoherence(coherence);
    document.getElementById('water-state').textContent = waterState;
    
    // Update harmonic theme
    const harmonicTheme = this.getHarmonicThemeFromCoherence(coherence);
    document.getElementById('harmonic-theme').textContent = harmonicTheme;
    
    // Update node resonance
    this.updateNodeResonance(coherence);
  }
  
  getWaterStateFromCoherence(coherence) {
    if (coherence > 0.8) return 'Harmonious Flow';
    if (coherence > 0.6) return 'Balanced';
    if (coherence > 0.4) return 'Turbulent';
    return 'Frozen';
  }
  
  getHarmonicThemeFromCoherence(coherence) {
    if (coherence > 0.8) return 'Perfect Fifth';
    if (coherence > 0.6) return 'Major Third';
    if (coherence > 0.4) return 'Minor Third';
    return 'Tritone';
  }
  
  updateNodeResonance(coherence) {
    this.nodes.forEach(node => {
      const baseResonance = node.userData.currentResonance;
      const adjustedResonance = baseResonance * coherence;
      
      // Update glow opacity
      const glow = node.children[0];
      if (glow && glow.material) {
        glow.material.opacity = 0.3 * adjustedResonance;
      }
      
      // Update emissive intensity
      node.material.emissiveIntensity = 0.25 * adjustedResonance;
    });
  }
  
  resetResonance() {
    // Reset all sliders to 0.5
    const sliders = document.querySelectorAll('.slider-container');
    sliders.forEach(slider => {
      const track = slider.querySelector('.slider-track');
      const thumb = slider.querySelector('.slider-thumb');
      const valueDisplay = slider.parentElement.querySelector('.axis-value');
      
      track.style.width = '50%';
      thumb.style.left = '50%';
      valueDisplay.textContent = '0.50';
    });
    
    // Reset resonance state
    this.resonanceState = {
      'fear-trust': 0.5,
      'pattern-flow': 0.5,
      'ownership-stewardship': 0.5,
      'protection-openness': 0.5,
      'noise-harmony': 0.5
    };
    
    // Update display
    this.updateResonance('overall', 0.5);
  }
  
  animateWaterCycle() {
    // Animate through water states
    const waterStates = ['Plasma', 'Vapor', 'Liquid', 'Ice', 'Structured', 'Clustered', 'Supercritical'];
    let currentState = 0;
    
    const cycle = setInterval(() => {
      const state = waterStates[currentState];
      
      // Update all nodes to current water state
      this.nodes.forEach(node => {
        node.userData.waterState = state;
        // Update color based on new water state
        const newColor = this.getWaterStateColor(state);
        node.material.color.setHex(newColor);
        node.material.emissive.setHex(newColor);
      });
      
      currentState = (currentState + 1) % waterStates.length;
      
      // Stop after one complete cycle
      if (currentState === 0) {
        clearInterval(cycle);
        // Restore original water states
        this.restoreOriginalWaterStates();
      }
    }, 500);
  }
  
  getWaterStateColor(waterState) {
    const palette = {
      Ice: 0x6db7ff,
      Liquid: 0xaee0ff,
      Vapor: 0xffd480,
      Plasma: 0xff7a7a,
      Structured: 0x9cd1ff,
      Clustered: 0xc9a0ff,
      Supercritical: 0xff9db5
    };
    return palette[waterState] || 0xffffff;
  }
  
  restoreOriginalWaterStates() {
    // Restore original water states from node data
    this.nodes.forEach(node => {
      const originalColor = node.userData.originalColor;
      node.material.color.setHex(originalColor);
      node.material.emissive.setHex(originalColor);
    });
  }
  
  createAttentionWave(x, y) {
    // Create ripple effect at mouse position
    const waveGeometry = new THREE.RingGeometry(0, 2, 16);
    const waveMaterial = new THREE.MeshBasicMaterial({
      color: 0x00ffff,
      transparent: true,
      opacity: 0.3
    });
    
    const wave = new THREE.Mesh(waveGeometry, waveMaterial);
    wave.position.set(x, y, 0);
    wave.userData = { age: 0, maxAge: 60 };
    
    this.scene.add(wave);
    
    // Remove wave after animation
    setTimeout(() => {
      this.scene.remove(wave);
    }, 1000);
  }
  
  handleNodeClick(mouse) {
    // Raycast to find clicked node
    const raycaster = new THREE.Raycaster();
    raycaster.setFromCamera(mouse, this.camera);
    
    const intersects = raycaster.intersectObjects(this.nodes);
    if (intersects.length > 0) {
      const node = intersects[0].object;
      this.focusNode(node);
    }
  }
  
  focusNode(node) {
    // Highlight focused node
    node.material.emissiveIntensity = 0.8;
    
    // Create focus effect
    const focusRing = new THREE.Mesh(
      new THREE.RingGeometry(0.5, 0.7, 16),
      new THREE.MeshBasicMaterial({
        color: 0x00ffff,
        transparent: true,
        opacity: 0.6
      })
    );
    focusRing.position.copy(node.position);
    focusRing.position.z = 0.1;
    
    this.scene.add(focusRing);
    
    // Remove focus effect after delay
    setTimeout(() => {
      this.scene.remove(focusRing);
      node.material.emissiveIntensity = 0.25 * node.userData.currentResonance;
    }, 2000);
  }
  
  onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }
  
  animate() {
    requestAnimationFrame(() => this.animate());
    
    const time = this.clock.getElapsedTime();
    
    // Animate sacred geometries
    this.geometries.flowerOfLife.rotation.z = time * 0.1;
    this.geometries.icositetragon.rotation.z = -time * 0.05;
    this.geometries.metatronCube.rotation.z = time * 0.02;
    
    // Animate nodes with resonance
    this.nodes.forEach((node, i) => {
      const resonance = node.userData.currentResonance;
      node.rotation.y = time * 0.2 * resonance;
      
      // Subtle floating motion
      node.position.y += Math.sin(time * 2 + i) * 0.001 * resonance;
    });
    
    // Animate edges with ripple effect
    this.edges.forEach((edge, i) => {
      const material = edge.material;
      material.opacity = 0.4 + Math.sin(time * 3 + i) * 0.1;
    });
    
    // Update resonance light
    this.resonanceLight.intensity = 1 + Math.sin(time * 4) * 0.3;
    
    this.renderer.render(this.scene, this.camera);
  }
}

// Initialize visualization
const viz = new LivingCodexViz();