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
    
      // Phase 3: Community Resonance Features
  this.communityResonance = {
    users: new Map(), // User ID -> resonance state
    collectiveTuning: new Map(), // Node ID -> collective resonance
    contributionHistory: [], // Array of tuning acts
    aiAgent: {
      active: false,
      currentPrompt: '',
      response: '',
      nodeFocus: null
    }
  };

  // Phase 4: Federation Integration
  this.federationClient = {
    baseUrl: 'http://localhost:8787',
    async fetchContributions(nodeId) {
      try {
        const response = await fetch(`${this.baseUrl}/contributions/node/${nodeId}`);
        if (response.ok) {
          return await response.json();
        }
        return { contributions: [], count: 0 };
      } catch (error) {
        console.error(`Error fetching contributions for ${nodeId}:`, error);
        return { contributions: [], count: 0 };
      }
    },
    async postContribution(contribution) {
      try {
        const activity = {
          type: 'Create',
          actor: 'viz@localhost',
          object: {
            type: 'Contribution',
            nodeId: contribution.nodeId,
            content: contribution.content,
            resonance: contribution.resonance
          }
        };
        
        const response = await fetch(`${this.baseUrl}/inbox`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/activity+json' },
          body: JSON.stringify(activity)
        });
        
        return response.ok;
      } catch (error) {
        console.error('Error posting contribution:', error);
        return false;
      }
    },
    async getStorageStats() {
      try {
        const response = await fetch(`${this.baseUrl}/storage/stats`);
        if (response.ok) {
          return await response.json();
        }
        return null;
      } catch (error) {
        console.error('Error fetching storage stats:', error);
        return null;
      }
    }
  };
    
    // Phase 3: Enhanced Resonance Dynamics
    this.resonanceLayers = {
      personal: new Map(), // Personal resonance state
      community: new Map(), // Community resonance overlay
      ai: new Map(), // AI agent resonance suggestions
      historical: new Map() // Historical resonance patterns
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
    
      // Phase 3: Create community resonance overlay
  this.createCommunityOverlay();
  
  // Phase 4: Initialize federation integration
  this.initializeFederationIntegration();
    
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
      
      // Phase 3: Initialize resonance layers for each node
      this.initializeResonanceLayers(nodeData.id);
    });
  }
  
  // Phase 3: Initialize resonance layers for a node
  initializeResonanceLayers(nodeId) {
    this.resonanceLayers.personal.set(nodeId, 0.5);
    this.resonanceLayers.community.set(nodeId, 0.5);
    this.resonanceLayers.ai.set(nodeId, 0.5);
    this.resonanceLayers.historical.set(nodeId, 0.5);
  }
  
  // Phase 3: Community resonance overlay system
  createCommunityOverlay() {
    // Create community resonance visualization
    this.nodes.forEach(node => {
      const nodeId = node.userData.id;
      const communityResonance = this.resonanceLayers.community.get(nodeId) || 0.5;
      
      // Create community resonance ring
      const ringGeometry = new THREE.RingGeometry(0.5, 0.6, 16);
      const ringMaterial = new THREE.MeshBasicMaterial({
        color: 0x00ff88,
        transparent: true,
        opacity: 0.3 * communityResonance
      });
      
      const communityRing = new THREE.Mesh(ringGeometry, ringMaterial);
      communityRing.position.copy(node.position);
      communityRing.position.z = 0.2;
      communityRing.userData = { type: 'community-overlay', nodeId: nodeId };
      
      this.scene.add(communityRing);
      node.userData.communityRing = communityRing;
    });
  }
  
  // Phase 3: Update community resonance for a node
  updateCommunityResonance(nodeId, newResonance, userId = 'anonymous') {
    const currentResonance = this.resonanceLayers.community.get(nodeId) || 0.5;
    const updatedResonance = (currentResonance + newResonance) / 2;
    
    this.resonanceLayers.community.set(nodeId, updatedResonance);
    
    // Record contribution
    this.communityResonance.contributionHistory.push({
      timestamp: Date.now(),
      userId: userId,
      nodeId: nodeId,
      oldResonance: currentResonance,
      newResonance: newResonance,
      collectiveResonance: updatedResonance
    });
    
    // Update visual representation
    this.updateCommunityOverlay(nodeId, updatedResonance);
    
    // Trigger AI agent response if significant change
    if (Math.abs(newResonance - currentResonance) > 0.2) {
      this.triggerAIResponse(nodeId, newResonance, userId);
    }
  }
  
  // Phase 3: Update community overlay visualization
  updateCommunityOverlay(nodeId, resonance) {
    const node = this.nodes.find(n => n.userData.id === nodeId);
    if (node && node.userData.communityRing) {
      const ring = node.userData.communityRing;
      ring.material.opacity = 0.3 * resonance;
      
      // Color shift based on resonance level
      if (resonance > 0.7) {
        ring.material.color.setHex(0x00ff88); // Green for high resonance
      } else if (resonance > 0.4) {
        ring.material.color.setHex(0xffff44); // Yellow for medium resonance
      } else {
        ring.material.color.setHex(0xff4444); // Red for low resonance
      }
    }
  }

  // Phase 4: Initialize federation integration
  async initializeFederationIntegration() {
    try {
      // Fetch initial community data
      await this.refreshCommunityData();
      
      // Set up periodic refresh
      setInterval(() => this.refreshCommunityData(), 10000); // Refresh every 10 seconds
      
      console.log('✓ Federation integration initialized');
    } catch (error) {
      console.error('Error initializing federation integration:', error);
    }
  }

  // Phase 4: Refresh community data from federation server
  async refreshCommunityData() {
    try {
      // Fetch contributions for each node
      for (const node of this.nodes) {
        const nodeId = node.userData.id;
        const data = await this.federationClient.fetchContributions(nodeId);
        
        if (data.contributions && data.contributions.length > 0) {
          // Calculate collective resonance from contributions
          const totalResonance = data.contributions.reduce((sum, contrib) => sum + contrib.resonance, 0);
          const avgResonance = totalResonance / data.contributions.length;
          
          // Update community resonance layer
          this.resonanceLayers.community.set(nodeId, avgResonance);
          
          // Update community overlay
          this.updateCommunityOverlay(nodeId, avgResonance);
          
          // Store contribution count for display
          node.userData.contributionCount = data.count;
        }
      }
      
      // Update storage stats display
      await this.updateStorageStatsDisplay();
      
    } catch (error) {
      console.error('Error refreshing community data:', error);
    }
  }

  // Phase 4: Update storage stats display
  async updateStorageStatsDisplay() {
    try {
      const stats = await this.federationClient.getStorageStats();
      if (stats) {
        // Update UI with storage statistics
        this.updateCommunityStats(stats);
      }
    } catch (error) {
      console.error('Error updating storage stats:', error);
    }
  }

  // Phase 4: Update community statistics display
  updateCommunityStats(stats) {
    // Find or create stats display element
    let statsElement = document.getElementById('community-stats');
    if (!statsElement) {
      statsElement = document.createElement('div');
      statsElement.id = 'community-stats';
      statsElement.className = 'community-stats';
      statsElement.innerHTML = `
        <h3>Community Statistics</h3>
        <p>Total Contributions: <span id="total-contributions">${stats.totalContributions}</span></p>
        <p>Active Nodes: <span id="total-nodes">${stats.totalNodes}</span></p>
        <p>Active Users: <span id="total-users">${stats.totalUsers}</span></p>
        <p>Storage Size: <span id="total-size">${(stats.totalSize / 1024).toFixed(1)} KB</span></p>
      `;
      
      // Add to the community panel
      const communityPanel = document.getElementById('community-panel');
      if (communityPanel) {
        communityPanel.appendChild(statsElement);
      }
    } else {
      // Update existing stats
      document.getElementById('total-contributions').textContent = stats.totalContributions;
      document.getElementById('total-nodes').textContent = stats.totalNodes;
      document.getElementById('total-users').textContent = stats.totalUsers;
      document.getElementById('total-size').textContent = (stats.totalSize / 1024).toFixed(1) + ' KB';
    }
  }

  // Phase 4: Post contribution from visualization
  async postContribution(nodeId, content, resonance) {
    try {
      const success = await this.federationClient.postContribution({
        nodeId,
        content,
        resonance
      });
      
      if (success) {
        // Refresh community data to show new contribution
        await this.refreshCommunityData();
        
        // Create visual feedback
        this.createContributionFeedback(nodeId, content);
        
        return true;
      } else {
        console.error('Failed to post contribution');
        return false;
      }
    } catch (error) {
      console.error('Error posting contribution:', error);
      return false;
    }
  }

  // Phase 4: Create visual feedback for new contribution
  createContributionFeedback(nodeId, content) {
    const node = this.nodes.find(n => n.userData.id === nodeId);
    if (node) {
      // Create contribution particle effect
      const particleGeometry = new THREE.SphereGeometry(0.1, 8, 8);
      const particleMaterial = new THREE.MeshBasicMaterial({
        color: 0x00ff88,
        transparent: true,
        opacity: 0.8
      });
      
      const particle = new THREE.Mesh(particleGeometry, particleMaterial);
      particle.position.copy(node.position);
      particle.position.z = 0.5;
      
      this.scene.add(particle);
      
      // Animate particle
      const startTime = Date.now();
      const animate = () => {
        const elapsed = Date.now() - startTime;
        const progress = elapsed / 2000; // 2 second animation
        
        if (progress < 1) {
          particle.position.y += 0.02;
          particle.material.opacity = 0.8 * (1 - progress);
          particle.scale.setScalar(1 + progress);
          requestAnimationFrame(animate);
        } else {
          this.scene.remove(particle);
        }
      };
      
      animate();
    }
  }
  
  // Phase 3: AI Agent Integration - Mirror Librarian
  triggerAIResponse(nodeId, resonance, userId) {
    this.communityResonance.aiAgent.active = true;
    this.communityResonance.aiAgent.nodeFocus = nodeId;
    
    // Generate AI response based on resonance change
    const response = this.generateAIResponse(nodeId, resonance, userId);
    this.communityResonance.aiAgent.response = response;
    
    // Update AI resonance layer
    this.resonanceLayers.ai.set(nodeId, resonance);
    
    // Create AI response visualization
    this.createAIResponseVisual(nodeId, response);
    
    // Update UI
    this.updateAIAgentUI();
  }
  
  // Phase 3: Generate AI response using mirror-librarian prompts
  generateAIResponse(nodeId, resonance, userId) {
    const node = this.nodes.find(n => n.userData.id === nodeId);
    const nodeName = nodeId.replace('codex:', '');
    
    let response = '';
    
    if (resonance > 0.7) {
      response = `🌊 High resonance detected in ${nodeName}! The community's collective tuning is creating harmonious flow. Consider exploring the nested wisdom within this node.`;
    } else if (resonance < 0.3) {
      response = `🌊 Low resonance in ${nodeName} suggests a need for collective attention. This node may benefit from community exploration and shared insights.`;
    } else {
      response = `🌊 Balanced resonance in ${nodeName}. The community is maintaining equilibrium. Consider deepening the exploration to reveal hidden patterns.`;
    }
    
    // Add archetypal guidance
    response += `\n\n🔮 Archetypal Prompt: "Expand ${nodeName} into three subnodes across scientific, symbolic, and water-state lenses. What new edges emerge?"`;
    
    return response;
  }
  
  // Phase 3: Create AI response visualization
  createAIResponseVisual(nodeId, response) {
    const node = this.nodes.find(n => n.userData.id === nodeId);
    if (!node) return;
    
    // Create floating text or particle effect
    const aiParticles = new THREE.Points(
      new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(0, 0, 0),
        new THREE.Vector3(0.5, 0.5, 0),
        new THREE.Vector3(-0.5, 0.5, 0),
        new THREE.Vector3(0.5, -0.5, 0),
        new THREE.Vector3(-0.5, -0.5, 0)
      ]),
      new THREE.PointsMaterial({
        color: 0x00ffff,
        size: 0.1,
        transparent: true,
        opacity: 0.8
      })
    );
    
    aiParticles.position.copy(node.position);
    aiParticles.position.z = 0.3;
    aiParticles.userData = { type: 'ai-response', nodeId: nodeId, response: response };
    
    this.scene.add(aiParticles);
    node.userData.aiParticles = aiParticles;
    
    // Animate AI particles
    this.animateAIParticles(aiParticles);
  }
  
  // Phase 3: Animate AI response particles
  animateAIParticles(particles) {
    const time = this.clock.getElapsedTime();
    
    particles.rotation.z = time * 0.5;
    particles.position.y += Math.sin(time * 3) * 0.001;
    
    // Remove particles after animation
    setTimeout(() => {
      if (particles.parent) {
        particles.parent.remove(particles);
      }
    }, 5000);
  }
  
  // Phase 3: Update AI Agent UI
  updateAIAgentUI() {
    const aiPanel = document.getElementById('ai-agent-panel');
    if (aiPanel) {
      const responseElement = aiPanel.querySelector('.ai-response');
      if (responseElement) {
        responseElement.textContent = this.communityResonance.aiAgent.response;
      }
    }
  }
  
  // Phase 3: Enhanced Resonance Dynamics with Community Integration
  updateResonance(axis, value) {
    // Update personal resonance state
    this.resonanceState[axis] = value;
    
    // Calculate overall coherence with community integration
    const axes = ['fear-trust', 'pattern-flow', 'ownership-stewardship', 'protection-openness', 'noise-harmony'];
    const personalValues = axes.map(ax => this.resonanceState[ax] || 0.5);
    const communityValues = axes.map(ax => this.getCommunityAxisResonance(ax));
    
    // Blend personal and community resonance
    const blendedValues = personalValues.map((personal, i) => 
      (personal * 0.6) + (communityValues[i] * 0.4)
    );
    
    const coherence = blendedValues.reduce((sum, val) => sum + (1 - Math.abs(0.5 - val) * 2), 0) / blendedValues.length;
    
    // Update display
    document.getElementById('coherence-score').textContent = coherence.toFixed(2);
    
    // Update water state based on coherence
    const waterState = this.getWaterStateFromCoherence(coherence);
    document.getElementById('water-state').textContent = waterState;
    
    // Update harmonic theme
    const harmonicTheme = this.getHarmonicThemeFromCoherence(coherence);
    document.getElementById('harmonic-theme').textContent = harmonicTheme;
    
    // Update node resonance with community overlay
    this.updateNodeResonanceWithCommunity(coherence);
    
    // Update community contribution display
    this.updateCommunityContributionDisplay();
  }
  
  // Phase 3: Get community axis resonance
  getCommunityAxisResonance(axis) {
    // This would integrate with actual community data
    // For now, return a simulated community resonance
    return 0.5 + Math.sin(Date.now() * 0.001) * 0.2;
  }
  
  // Phase 3: Update node resonance with community integration
  updateNodeResonanceWithCommunity(coherence) {
    this.nodes.forEach(node => {
      const nodeId = node.userData.id;
      const baseResonance = node.userData.currentResonance;
      const communityResonance = this.resonanceLayers.community.get(nodeId) || 0.5;
      const aiResonance = this.resonanceLayers.ai.get(nodeId) || 0.5;
      
      // Multi-layered resonance calculation
      const personalLayer = baseResonance * coherence;
      const communityLayer = communityResonance * 0.3;
      const aiLayer = aiResonance * 0.2;
      
      const adjustedResonance = personalLayer + communityLayer + aiLayer;
      
      // Update glow opacity
      const glow = node.children[0];
      if (glow && glow.material) {
        glow.material.opacity = 0.3 * adjustedResonance;
      }
      
      // Update emissive intensity
      node.material.emissiveIntensity = 0.25 * adjustedResonance;
      
      // Update community ring if exists
      if (node.userData.communityRing) {
        const ring = node.userData.communityRing;
        ring.material.opacity = 0.3 * communityResonance;
      }
    });
  }
  
  // Phase 3: Community contribution system
  contributeToNode(nodeId, contribution) {
    const { resonance, insight, userId } = contribution;
    
    // Update community resonance
    this.updateCommunityResonance(nodeId, resonance, userId);
    
    // Record detailed contribution
    const contributionRecord = {
      timestamp: Date.now(),
      userId: userId,
      nodeId: nodeId,
      resonance: resonance,
      insight: insight,
      type: 'community-contribution'
    };
    
    this.communityResonance.contributionHistory.push(contributionRecord);
    
    // Trigger community resonance wave
    this.createCommunityResonanceWave(nodeId, resonance);
    
    // Update contribution display
    this.updateCommunityContributionDisplay();
  }
  
  // Phase 3: Create community resonance wave
  createCommunityResonanceWave(nodeId, resonance) {
    const node = this.nodes.find(n => n.userData.id === nodeId);
    if (!node) return;
    
    // Create expanding ring wave
    const waveGeometry = new THREE.RingGeometry(0.8, 1.2, 32);
    const waveMaterial = new THREE.MeshBasicMaterial({
      color: 0x00ff88,
      transparent: true,
      opacity: 0.6 * resonance
    });
    
    const wave = new THREE.Mesh(waveGeometry, waveMaterial);
    wave.position.copy(node.position);
    wave.position.z = 0.1;
    wave.userData = { type: 'community-wave', age: 0, maxAge: 60 };
    
    this.scene.add(wave);
    
    // Animate wave expansion
    this.animateCommunityWave(wave);
  }
  
  // Phase 3: Animate community resonance wave
  animateCommunityWave(wave) {
    const animate = () => {
      wave.userData.age++;
      const progress = wave.userData.age / wave.userData.maxAge;
      
      // Expand ring
      wave.scale.setScalar(1 + progress * 2);
      
      // Fade out
      wave.material.opacity = 0.6 * (1 - progress);
      
      if (wave.userData.age < wave.userData.maxAge) {
        requestAnimationFrame(animate);
      } else {
        if (wave.parent) {
          wave.parent.remove(wave);
        }
      }
    };
    
    animate();
  }
  
  // Phase 3: Update community contribution display
  updateCommunityContributionDisplay() {
    const contributionPanel = document.getElementById('community-contributions');
    if (contributionPanel) {
      const recentContributions = this.communityResonance.contributionHistory
        .slice(-5)
        .reverse();
      
      contributionPanel.innerHTML = recentContributions.map(contribution => `
        <div class="contribution-item">
          <span class="contribution-user">${contribution.userId}</span>
          <span class="contribution-node">${contribution.nodeId}</span>
          <span class="contribution-resonance">${contribution.resonance.toFixed(2)}</span>
        </div>
      `).join('');
    }
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
    
    // Phase 3: Enhanced Controls
    // Toggle community overlay visibility
    document.getElementById('toggle-community').addEventListener('click', () => {
      this.toggleCommunityOverlay();
    });
    
    // AI insight generation
    document.getElementById('ai-insight').addEventListener('click', () => {
      this.generateAIInsight();
    });
    
    // Open contribution modal
    document.getElementById('contribute').addEventListener('click', () => {
      document.getElementById('contribution-modal').classList.add('show');
    });
    
    // Submit contribution
    document.getElementById('submit-contribution').addEventListener('click', () => {
      this.submitContribution();
    });
    
    // Cancel contribution
    document.getElementById('cancel-contribution').addEventListener('click', () => {
      document.getElementById('contribution-modal').classList.remove('show');
    });
    
    // AI Agent Actions
    document.getElementById('expand-node').addEventListener('click', () => {
      this.expandNodeWithAI();
    });
    
    document.getElementById('archetypal-guidance').addEventListener('click', () => {
      this.getArchetypalGuidance();
    });
    
    document.getElementById('water-state-insight').addEventListener('click', () => {
      this.getWaterStateInsight();
    });
    
    // Contribution resonance slider
    const contributionResonance = document.getElementById('contribution-resonance');
    const resonanceValue = document.querySelector('.resonance-value');
    if (contributionResonance && resonanceValue) {
      contributionResonance.addEventListener('input', (e) => {
        resonanceValue.textContent = parseFloat(e.target.value).toFixed(2);
      });
    }
  }
  
  // Phase 3: Toggle community overlay visibility
  toggleCommunityOverlay() {
    this.nodes.forEach(node => {
      if (node.userData.communityRing) {
        node.userData.communityRing.visible = !node.userData.communityRing.visible;
      }
    });
  }
  
  // Phase 3: Generate AI insight for current state
  generateAIInsight() {
    const currentCoherence = parseFloat(document.getElementById('coherence-score').textContent);
    const insight = this.generateAIResponse('overall', currentCoherence, 'system');
    
    // Update AI panel
    this.communityResonance.aiAgent.response = insight;
    this.updateAIAgentUI();
    
    // Create insight visualization
    this.createInsightVisualization(insight);
  }
  
  // Phase 3: Create insight visualization
  createInsightVisualization(insight) {
    // Create floating insight particles
    const insightParticles = new THREE.Points(
      new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(0, 0, 0),
        new THREE.Vector3(1, 1, 0),
        new THREE.Vector3(-1, 1, 0),
        new THREE.Vector3(1, -1, 0),
        new THREE.Vector3(-1, -1, 0)
      ]),
      new THREE.PointsMaterial({
        color: 0xff00ff,
        size: 0.15,
        transparent: true,
        opacity: 0.8
      })
    );
    
    insightParticles.position.set(0, 0, 10);
    insightParticles.userData = { type: 'insight-visualization' };
    
    this.scene.add(insightParticles);
    
    // Animate insight particles
    this.animateInsightParticles(insightParticles);
  }
  
  // Phase 3: Animate insight particles
  animateInsightParticles(particles) {
    const time = this.clock.getElapsedTime();
    
    particles.rotation.z = time * 0.3;
    particles.position.y = Math.sin(time * 2) * 2;
    
    // Remove after animation
    setTimeout(() => {
      if (particles.parent) {
        particles.parent.remove(particles);
      }
    }, 8000);
  }
  
  // Phase 3: Submit contribution from modal
  submitContribution() {
    const nodeId = document.getElementById('contribution-node').value;
    const resonance = parseFloat(document.getElementById('contribution-resonance').value);
    const insight = document.getElementById('contribution-insight').value;
    const userId = document.getElementById('contribution-user').value;
    
    if (!insight.trim()) {
      alert('Please provide an insight for your contribution.');
      return;
    }
    
    // Submit contribution
    this.contributeToNode(nodeId, {
      resonance: resonance,
      insight: insight,
      userId: userId
    });
    
    // Close modal
    document.getElementById('contribution-modal').classList.remove('show');
    
    // Clear form
    document.getElementById('contribution-insight').value = '';
    document.getElementById('contribution-resonance').value = '0.5';
    document.querySelector('.resonance-value').textContent = '0.50';
  }
  
  // Phase 3: Expand node with AI guidance
  expandNodeWithAI() {
    const focusedNode = this.communityResonance.aiAgent.nodeFocus || 'codex:Void';
    const nodeName = focusedNode.replace('codex:', '');
    
    const expansionPrompt = `🔮 Expanding ${nodeName} into three subnodes:
    
1. **Scientific Lens**: What empirical patterns or measurable phenomena does ${nodeName} represent?
2. **Symbolic Lens**: What archetypal symbols or cultural meanings does ${nodeName} embody?
3. **Water-State Lens**: What fluid dynamics or phase transitions does ${nodeName} manifest?

Each subnode should reveal deeper wisdom and create new resonance pathways.`;
    
    this.communityResonance.aiAgent.response = expansionPrompt;
    this.updateAIAgentUI();
  }
  
  // Phase 3: Get archetypal guidance
  getArchetypalGuidance() {
    const guidance = `🔮 Archetypal Guidance for the Living Codex:
    
**The Hero's Journey**: Each node represents a stage in the collective consciousness journey.
**The Wise Old One**: The AI agent serves as a mirror, reflecting back the community's wisdom.
**The Trickster**: Embrace paradox and contradiction as sources of creative tension.
**The Creator**: Every contribution shapes the evolving knowledge landscape.
**The Destroyer**: Let go of rigid structures to allow new patterns to emerge.`;
    
    this.communityResonance.aiAgent.response = guidance;
    this.updateAIAgentUI();
  }
  
  // Phase 3: Get water state insight
  getWaterStateInsight() {
    const currentWaterState = document.getElementById('water-state').textContent;
    const insight = `🌊 Water State Insight: ${currentWaterState}
    
**Current State**: The community is experiencing ${currentWaterState.toLowerCase()} resonance.
**Flow Dynamics**: This state reflects the collective emotional and intellectual climate.
**Transition Potential**: Consider what conditions would facilitate movement to the next water state.
**Resonance Patterns**: Notice how individual contributions ripple through the collective field.
**Harmonic Alignment**: The current state suggests ${this.getHarmonicThemeFromCoherence(0.7)} as the optimal tuning frequency.`;
    
    this.communityResonance.aiAgent.response = insight;
    this.updateAIAgentUI();
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
    
    // Phase 4: Show node details and contributions
    this.showNodeDetails(node);
    
    // Remove focus effect after delay
    setTimeout(() => {
      this.scene.remove(focusRing);
      node.material.emissiveIntensity = 0.25 * node.userData.currentResonance;
    }, 2000);
  }

  // Phase 4: Show node details and contributions
  async showNodeDetails(node) {
    const nodeId = node.userData.id;
    
    // Fetch contributions for this node
    const data = await this.federationClient.fetchContributions(nodeId);
    
    // Create or update node details panel
    let detailsPanel = document.getElementById('node-details');
    if (!detailsPanel) {
      detailsPanel = document.createElement('div');
      detailsPanel.id = 'node-details';
      detailsPanel.className = 'node-details';
      document.body.appendChild(detailsPanel);
    }
    
    // Update panel content
    detailsPanel.innerHTML = `
      <div class="node-details-content">
        <h3>${node.userData.name || nodeId}</h3>
        <p><strong>Water State:</strong> ${node.userData.waterState || 'Unknown'}</p>
        <p><strong>Archetype:</strong> ${(node.userData.archetype || []).join(', ') || 'None'}</p>
        <p><strong>Community Contributions:</strong> ${data.count || 0}</p>
        <p><strong>Community Resonance:</strong> ${(this.resonanceLayers.community.get(nodeId) || 0.5).toFixed(2)}</p>
        
        <div class="contributions-list">
          <h4>Recent Contributions:</h4>
          ${data.contributions && data.contributions.length > 0 ? 
            data.contributions.slice(0, 3).map(contrib => `
              <div class="contribution-item">
                <p><strong>${contrib.userId}:</strong> ${contrib.content}</p>
                <p class="contribution-meta">Resonance: ${contrib.resonance.toFixed(2)} | ${new Date(contrib.timestamp).toLocaleString()}</p>
              </div>
            `).join('') : 
            '<p>No contributions yet</p>'
          }
        </div>
        
        <div class="contribute-form">
          <h4>Add Contribution:</h4>
          <textarea id="contribution-content" placeholder="Share your insight about this node..." rows="3"></textarea>
          <div class="resonance-slider">
            <label>Resonance: <span id="resonance-value">0.5</span></label>
            <input type="range" id="resonance-slider" min="0" max="1" step="0.01" value="0.5">
          </div>
          <button onclick="viz.submitContribution('${nodeId}')">Submit Contribution</button>
        </div>
        
        <button class="close-btn" onclick="document.getElementById('node-details').remove()">Close</button>
      </div>
    `;
    
    // Set up resonance slider
    const slider = document.getElementById('resonance-slider');
    const value = document.getElementById('resonance-value');
    if (slider && value) {
      slider.addEventListener('input', (e) => {
        value.textContent = e.target.value;
      });
    }
    
    // Position panel
    detailsPanel.style.display = 'block';
  }

  // Phase 4: Submit contribution from node details
  async submitContribution(nodeId) {
    const content = document.getElementById('contribution-content')?.value;
    const resonance = parseFloat(document.getElementById('resonance-slider')?.value || '0.5');
    
    if (!content || content.trim() === '') {
      alert('Please enter a contribution');
      return;
    }
    
    const success = await this.postContribution(nodeId, content.trim(), resonance);
    if (success) {
      alert('Contribution submitted successfully!');
      document.getElementById('contribution-content').value = '';
      document.getElementById('resonance-slider').value = '0.5';
      document.getElementById('resonance-value').textContent = '0.5';
      
      // Refresh node details
      const node = this.nodes.find(n => n.userData.id === nodeId);
      if (node) {
        this.showNodeDetails(node);
      }
    } else {
      alert('Failed to submit contribution. Please try again.');
    }
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