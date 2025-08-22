#!/usr/bin/env python3
"""
GitHub Repository Setup Script
Automates the setup of the Living Codex ICE core repository
"""

import os
import subprocess
import json
from pathlib import Path

def setup_github_repo():
    """Set up GitHub repository for Living Codex ICE core"""
    print("🚀 Setting up GitHub repository for Living Codex ICE core...")
    
    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# ICE core specific
ice_core_repo/
ice_core_demo/
*.sqlite
*.db

# Environment variables
.env
.env.local
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Created .gitignore")
    
    # Initialize Git repository
    try:
        subprocess.run(['git', 'init'], check=True)
        print("✅ Initialized Git repository")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Added all files to Git")
        
        # Initial commit
        subprocess.run(['git', 'commit', '-m', 'Initial commit: Living Codex ICE core system'], check=True)
        print("✅ Created initial commit")
        
        print("\n🎉 GitHub repository setup complete!")
        print("\nNext steps:")
        print("1. Create repository on GitHub: https://github.com/new")
        print("2. Add remote origin: git remote add origin <your-repo-url>")
        print("3. Push to GitHub: git push -u origin main")
        print("4. Enable GitHub Actions for CI/CD")
        print("5. Set up repository secrets for deployment")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git setup failed: {e}")

if __name__ == "__main__":
    setup_github_repo()
