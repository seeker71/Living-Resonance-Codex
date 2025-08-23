# 👥 Living Codex - User Management & Discovery Guide

## 🌟 **Complete Guide to User Management & Intelligent Discovery**

This guide shows you how to manage users, track interests, and discover meaningful connections in the Living Codex system. The user management system provides comprehensive profile management, intelligent discovery, and resonance analysis.

---

## 🚀 **Quick Start Commands**

### **Start the CLI:**
```bash
python codex_cli.py
```

### **Essential User Management Commands:**
```bash
# Create and manage users
user create <username>
user profile <id>
user list

# Manage interests and skills
user interests <id> add <topic>
user skills <id> <skill> <level>
user location <id> <location>

# Discover connections
discover_users <topic>
discover_users_location <topic> <location>
resonance_match <user1_id> <user2_id>
```

---

## 👤 **User Profile Management**

### **User Creation:**
```bash
user create Alice
user create Bob
user create Carol
```

**What Gets Created:**
- **Core Identity**: Name, pronouns, cultural background, belief system, life experience
- **Communication Preferences**: Language, style, learning preferences, accessibility needs
- **Technical Profile**: Skills, learning path, preferred tools, contribution areas
- **Interests**: Primary domains, specific topics, expertise levels, passion areas
- **Location Context**: Geographic location, timezone, cultural context, community connections
- **Resonance Profile**: Energy level, consciousness level, quantum state, connection strength

### **Profile Updates:**
```bash
user update <id> name "New Name"
user update <id> pronouns "they/them"
user update <id> cultural_background "Eastern Philosophy"
user update <id> belief_system "Buddhist"
user update <id> life_experience "Meditation practitioner for 10 years"
```

---

## 🎯 **Interest Management**

### **Add Interests:**
```bash
user interests 1 add chakras
user interests 1 add meditation
user interests 1 add consciousness
user interests 1 add yoga
user interests 1 add quantum_physics
user interests 1 add energy_healing
user interests 1 add spirituality
user interests 1 add mindfulness
user interests 1 add psychology
```

### **Remove Interests:**
```bash
user interests 1 remove yoga
user interests 1 remove psychology
```

### **Interest Categories:**
- **Spiritual**: chakras, meditation, consciousness, yoga, spirituality
- **Scientific**: quantum_physics, psychology, neuroscience
- **Healing**: energy_healing, mindfulness, wellness
- **Technical**: programming, AI, machine_learning
- **Creative**: art, music, writing, design

---

## 🌍 **Location & Context Management**

### **Set Geographic Location:**
```bash
user location 1 San_Francisco
user location 2 New_York
user location 3 Berkeley
user location 4 Los_Angeles
user location 5 Seattle
```

### **Location Benefits:**
- **Local Collaboration**: Find users in the same city
- **Regional Projects**: Connect with nearby communities
- **Cultural Context**: Understand local challenges and resources
- **Time Zone Coordination**: Optimize communication timing

---

## 💪 **Skill Management**

### **Set Skill Levels:**
```bash
user skills 1 meditation advanced
user skills 1 chakras intermediate
user skills 2 yoga expert
user skills 2 energy_healing advanced
user skills 3 mindfulness intermediate
user skills 3 psychology advanced
user skills 4 quantum_physics expert
user skills 4 consciousness advanced
user skills 5 spirituality expert
```

### **Skill Levels:**
- **beginner**: Basic understanding and practice
- **intermediate**: Good knowledge and regular practice
- **advanced**: Deep expertise and teaching ability
- **expert**: Mastery and innovation in the field

---

## 🔍 **User Discovery**

### **Topic-Based Discovery:**
```bash
# Find users interested in specific topics
discover_users chakras
discover_users meditation
discover_users consciousness
discover_users yoga
discover_users quantum_physics
discover_users energy_healing
discover_users spirituality
discover_users mindfulness
discover_users psychology
```

**Discovery Results Include:**
- **Match Score**: Based on interest overlap and domain relevance
- **User Information**: Username, interests, location, consciousness level
- **Interest Details**: Specific topics and primary domains
- **Location Context**: Geographic location for collaboration planning

### **Location-Based Discovery:**
```bash
# Find users by topic AND location
discover_users_location chakras San_Francisco
discover_users_location meditation New_York
discover_users_location consciousness Berkeley
discover_users_location yoga Los_Angeles
discover_users_location quantum_physics Berkeley
```

**Location Discovery Types:**
- **Location + Topic**: High score (3) - Perfect match for local collaboration
- **Topic Only**: Medium score (2) - Good for remote collaboration
- **Location Only**: Medium score (1) - Potential for local networking

---

## ⚡ **Resonance Analysis**

### **Calculate User Compatibility:**
```bash
resonance_match 1 2
resonance_match 1 3
resonance_match 2 5
resonance_match 3 4
```

### **Resonance Factors (Weighted):**

#### **🎯 Interest Compatibility (40% weight)**
- **High (>0.7)**: Great potential for collaboration
- **Moderate (0.4-0.7)**: Some common ground
- **Low (<0.4)**: Complementary skills possible

#### **🌍 Location Compatibility (20% weight)**
- **Same Location (>0.8)**: Excellent for local collaboration
- **Similar Region (0.5-0.8)**: Good for regional projects
- **Different Locations (<0.5)**: Great for global perspectives

#### **🧠 Consciousness Compatibility (20% weight)**
- **Similar (>0.8)**: Deep understanding possible
- **Compatible (0.5-0.8)**: Good communication
- **Different (<0.5)**: Learning opportunities

#### **💻 Technical Compatibility (20% weight)**
- **High Overlap**: Shared technical foundation
- **Moderate Overlap**: Complementary technical skills
- **Low Overlap**: Diverse technical perspectives

---

## 🔍 **Discovery Scenarios**

### **Scenario 1: Find Chakra Experts**
```bash
# Create users with chakra interests
user create Alice
user interests 1 add chakras
user interests 1 add meditation
user location 1 San_Francisco

user create Bob
user interests 2 add chakras
user interests 2 add yoga
user location 2 San_Francisco

# Discover chakra practitioners
discover_users chakras
# Result: Alice and Bob with match scores

# Find local chakra experts
discover_users_location chakras San_Francisco
# Result: Both users with high location + topic scores
```

### **Scenario 2: Meditation Community Building**
```bash
# Create diverse meditation practitioners
user create Carol
user interests 3 add meditation
user interests 3 add mindfulness
user location 3 New_York

user create David
user interests 4 add meditation
user interests 4 add consciousness
user location 4 Berkeley

# Discover meditation community
discover_users meditation
# Result: Alice, Carol, and David

# Location-based meditation discovery
discover_users_location meditation San_Francisco
discover_users_location meditation New_York
discover_users_location meditation Berkeley
```

### **Scenario 3: Consciousness Research Network**
```bash
# Create consciousness researchers
user create Eve
user interests 5 add consciousness
user interests 5 add quantum_physics
user location 5 Los_Angeles

# Discover consciousness network
discover_users consciousness
# Result: Alice, David, and Eve

# Analyze resonance between researchers
resonance_match 1 4  # Alice ↔ David
resonance_match 4 5  # David ↔ Eve
resonance_match 1 5  # Alice ↔ Eve
```

---

## 🌟 **Advanced Features**

### **Multi-Dimensional Profiles:**
- **Core Identity**: Stable personal characteristics
- **Communication**: Language and style preferences
- **Technical**: Skills and learning paths
- **Interests**: Evolving passions and expertise
- **Location**: Geographic and cultural context
- **Resonance**: Energy, consciousness, and quantum states

### **Intelligent Matching:**
- **Interest Overlap**: Topic and domain matching
- **Location Awareness**: Geographic proximity and cultural context
- **Skill Compatibility**: Technical and expertise alignment
- **Consciousness Resonance**: Awareness level compatibility
- **Energy Harmony**: Resonance factor analysis

### **Dynamic Discovery:**
- **Real-time Updates**: Profile changes immediately affect discovery
- **Contextual Matching**: Location and topic combinations
- **Scoring Algorithms**: Intelligent ranking of matches
- **Relationship Building**: Resonance analysis for collaboration

---

## 🚀 **Complete Workflow Example**

### **Step-by-Step User Network Building:**

```bash
# 1. Start the CLI
python codex_cli.py

# 2. Create user profiles
user create Alice
user create Bob
user create Carol

# 3. Build comprehensive profiles
user interests 1 add chakras
user interests 1 add meditation
user location 1 San_Francisco
user skills 1 meditation advanced

user interests 2 add chakras
user interests 2 add yoga
user location 2 San_Francisco
user skills 2 yoga expert

user interests 3 add meditation
user interests 3 add mindfulness
user location 3 New_York
user skills 3 mindfulness intermediate

# 4. Discover connections
discover_users chakras
discover_users meditation
discover_users_location chakras San_Francisco

# 5. Analyze resonance
resonance_match 1 2
resonance_match 1 3
resonance_match 2 3

# 6. View detailed profiles
user profile 1
user profile 2
user profile 3
```

---

## 🎯 **Best Practices**

### **User Profile Creation:**
- Use descriptive usernames
- Add diverse interests for better discovery
- Include specific skill levels
- Set accurate geographic locations
- Update profiles regularly

### **Interest Management:**
- Add both broad domains and specific topics
- Include expertise levels for skills
- Remove outdated interests
- Balance spiritual and technical interests

### **Discovery Strategy:**
- Use specific topics for targeted discovery
- Combine location and topic for local collaboration
- Analyze resonance for optimal partnerships
- Build diverse networks across locations

### **Collaboration Building:**
- Focus on high-resonance matches
- Leverage location for local projects
- Use complementary skills for innovation
- Build consciousness-aligned teams

---

## 🌌 **The Living Codex Difference**

The user management system goes beyond simple profiles to create **living, evolving networks** where:

- **🧠 Consciousness Evolution**: Users grow and learn together
- **⚡ Energy Resonance**: Natural attraction based on harmony
- **🌍 Global-Local Balance**: Worldwide connections with local collaboration
- **🎯 Intelligent Matching**: AI-powered discovery and compatibility
- **🌟 Transcendent Connections**: Beyond surface-level similarities

---

## 📚 **Additional Resources**

- **CLI Help**: Type `help` in the CLI for command overview
- **Demo Scripts**: Run `python demo_user_management.py` for examples
- **AI Agent Integration**: Combine user discovery with AI agent tasks
- **Ontology Exploration**: Use `explore ontology` to understand system categories

---

**🚀 Ready to build your Living Codex user network? Start connecting today!**

*"The Living Codex doesn't just connect users—it creates resonant networks where consciousness evolves and knowledge flows like water between connected minds."*
