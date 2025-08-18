#!/usr/bin/env python3
import json
from pathlib import Path

SEED = Path(__file__).parents[2] / "ontology" / "seed.json"

def consonance(a):
    # Enhanced mapping using harmonic metaphors and water states
    x = a.get('default', 0.5)
    base_score = round(1 - abs(0.5 - x)*2, 3)
    
    # Bonus for harmonic metaphors
    if 'Perfect' in a.get('harmonicMetaphor', ''):
        base_score += 0.1
    elif 'Major' in a.get('harmonicMetaphor', ''):
        base_score += 0.05
    elif 'Minor' in a.get('harmonicMetaphor', ''):
        base_score += 0.03
    
    return min(1.0, round(base_score, 3))

def analyze_axes(axes):
    """Analyze the vibrational axes for coherence patterns"""
    analysis = {
        'total_axes': len(axes),
        'coherence_score': 0,
        'harmonic_themes': [],
        'water_themes': [],
        'balance_analysis': []
    }
    
    for ax in axes:
        score = consonance(ax)
        analysis['coherence_score'] += score
        
        # Extract harmonic themes
        if 'harmonicMetaphor' in ax:
            analysis['harmonic_themes'].append(ax['harmonicMetaphor'])
        
        # Extract water themes
        if 'waterMetaphor' in ax:
            analysis['water_themes'].append(ax['waterMetaphor'])
        
        # Analyze balance
        balance = 'balanced' if abs(ax.get('default', 0.5) - 0.5) < 0.1 else 'polarized'
        analysis['balance_analysis'].append({
            'axis': ax['name'],
            'balance': balance,
            'consonance': score
        })
    
    analysis['coherence_score'] = round(analysis['coherence_score'] / max(1, len(axes)), 3)
    return analysis

def main():
    data = json.loads(SEED.read_text())
    axes = data.get('axes', [])
    
    # Enhanced analysis
    analysis = analyze_axes(axes)
    
    print("=== Living Codex Resonance Analysis ===")
    print(f"Total Axes: {analysis['total_axes']}")
    print(f"Overall Coherence Score: {analysis['coherence_score']}")
    print(f"\nHarmonic Themes: {', '.join(analysis['harmonic_themes'])}")
    print(f"Water Metaphors: {', '.join(analysis['water_themes'])}")
    print(f"\nBalance Analysis:")
    for balance in analysis['balance_analysis']:
        print(f"  {balance['axis']}: {balance['balance']} (consonance: {balance['consonance']})")
    
    print(f"\nRaw Data: {json.dumps(analysis, indent=2)}")

if __name__ == '__main__':
    main()