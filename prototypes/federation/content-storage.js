#!/usr/bin/env node
/**
 * Content-Addressed Storage System for Living Codex Phase 4
 * Implements IPFS-like content addressing for community contributions
 */

import crypto from 'crypto';
import fs from 'fs/promises';
import path from 'path';

class ContentAddressedStorage {
  constructor(storagePath = './storage') {
    this.storagePath = storagePath;
    this.manifestPath = path.join(storagePath, 'manifest.json');
    this.contributionsPath = path.join(storagePath, 'contributions');
    this.ensureStorageExists();
  }

  async ensureStorageExists() {
    try {
      await fs.mkdir(this.storagePath, { recursive: true });
      await fs.mkdir(this.contributionsPath, { recursive: true });
      
      // Initialize manifest if it doesn't exist
      try {
        await fs.access(this.manifestPath);
      } catch {
        await this.saveManifest({
          version: '1.0.0',
          created: new Date().toISOString(),
          contributions: {},
          nodes: {},
          users: {}
        });
      }
    } catch (error) {
      console.error('Error initializing storage:', error);
    }
  }

  /**
   * Generate content hash for a contribution
   */
  generateContentHash(content) {
    const contentString = typeof content === 'string' ? content : JSON.stringify(content);
    return crypto.createHash('sha256').update(contentString).digest('hex');
  }

  /**
   * Store a community contribution with content addressing
   */
  async storeContribution(contribution) {
    try {
      // Generate content hash
      const contentHash = this.generateContentHash(contribution);
      
      // Create contribution file
      const contributionFile = path.join(this.contributionsPath, `${contentHash}.json`);
      
      // Add metadata
      const contributionWithMetadata = {
        ...contribution,
        contentHash,
        storedAt: new Date().toISOString(),
        size: JSON.stringify(contribution).length
      };

      // Store the contribution
      await fs.writeFile(contributionFile, JSON.stringify(contributionWithMetadata, null, 2));

      // Update manifest
      await this.updateManifest(contentHash, contributionWithMetadata);

      return {
        success: true,
        contentHash,
        url: `/contributions/${contentHash}`,
        size: contributionWithMetadata.size
      };
    } catch (error) {
      console.error('Error storing contribution:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Retrieve a contribution by content hash
   */
  async getContribution(contentHash) {
    try {
      const contributionFile = path.join(this.contributionsPath, `${contentHash}.json`);
      const content = await fs.readFile(contributionFile, 'utf8');
      return JSON.parse(content);
    } catch (error) {
      console.error(`Error retrieving contribution ${contentHash}:`, error);
      return null;
    }
  }

  /**
   * Update the storage manifest
   */
  async updateManifest(contentHash, contribution) {
    try {
      const manifest = await this.loadManifest();
      
      // Add contribution to manifest
      manifest.contributions[contentHash] = {
        nodeId: contribution.nodeId,
        userId: contribution.userId,
        type: contribution.type,
        storedAt: contribution.storedAt,
        size: contribution.size
      };

      // Update node statistics
      if (!manifest.nodes[contribution.nodeId]) {
        manifest.nodes[contribution.nodeId] = {
          contributionCount: 0,
          lastContribution: null,
          totalResonance: 0
        };
      }
      manifest.nodes[contribution.nodeId].contributionCount++;
      manifest.nodes[contribution.nodeId].lastContribution = contribution.storedAt;
      if (contribution.resonance) {
        manifest.nodes[contribution.nodeId].totalResonance += contribution.resonance;
      }

      // Update user statistics
      if (!manifest.users[contribution.userId]) {
        manifest.users[contribution.userId] = {
          contributionCount: 0,
          lastContribution: null,
          totalResonance: 0
        };
      }
      manifest.users[contribution.userId].contributionCount++;
      manifest.users[contribution.userId].lastContribution = contribution.storedAt;
      if (contribution.resonance) {
        manifest.users[contribution.userId].totalResonance += contribution.resonance;
      }

      await this.saveManifest(manifest);
    } catch (error) {
      console.error('Error updating manifest:', error);
    }
  }

  /**
   * Load the storage manifest
   */
  async loadManifest() {
    try {
      const content = await fs.readFile(this.manifestPath, 'utf8');
      return JSON.parse(content);
    } catch (error) {
      console.error('Error loading manifest:', error);
      return {
        version: '1.0.0',
        created: new Date().toISOString(),
        contributions: {},
        nodes: {},
        users: {}
      };
    }
  }

  /**
   * Save the storage manifest
   */
  async saveManifest(manifest) {
    try {
      await fs.writeFile(this.manifestPath, JSON.stringify(manifest, null, 2));
    } catch (error) {
      console.error('Error saving manifest:', error);
    }
  }

  /**
   * Get all contributions for a specific node
   */
  async getNodeContributions(nodeId) {
    try {
      const manifest = await this.loadManifest();
      const nodeContributions = [];
      
      for (const [hash, info] of Object.entries(manifest.contributions)) {
        if (info.nodeId === nodeId) {
          const contribution = await this.getContribution(hash);
          if (contribution) {
            nodeContributions.push(contribution);
          }
        }
      }
      
      return nodeContributions.sort((a, b) => new Date(b.storedAt) - new Date(a.storedAt));
    } catch (error) {
      console.error('Error getting node contributions:', error);
      return [];
    }
  }

  /**
   * Get all contributions from a specific user
   */
  async getUserContributions(userId) {
    try {
      const manifest = await this.loadManifest();
      const userContributions = [];
      
      for (const [hash, info] of Object.entries(manifest.contributions)) {
        if (info.userId === userId) {
          const contribution = await this.getContribution(hash);
          if (contribution) {
            userContributions.push(contribution);
          }
        }
      }
      
      return userContributions.sort((a, b) => new Date(b.storedAt) - new Date(a.storedAt));
    } catch (error) {
      console.error('Error getting user contributions:', error);
      return [];
    }
  }

  /**
   * Get storage statistics
   */
  async getStorageStats() {
    try {
      const manifest = await this.loadManifest();
      const totalContributions = Object.keys(manifest.contributions).length;
      const totalNodes = Object.keys(manifest.nodes).length;
      const totalUsers = Object.keys(manifest.users).length;
      
      let totalSize = 0;
      for (const [hash, info] of Object.entries(manifest.contributions)) {
        totalSize += info.size || 0;
      }

      return {
        totalContributions,
        totalNodes,
        totalUsers,
        totalSize,
        lastUpdated: manifest.lastUpdated || manifest.created
      };
    } catch (error) {
      console.error('Error getting storage stats:', error);
      return null;
    }
  }

  /**
   * Export storage for federation
   */
  async exportForFederation() {
    try {
      const manifest = await this.loadManifest();
      const exportData = {
        version: manifest.version,
        exportedAt: new Date().toISOString(),
        contributions: manifest.contributions,
        nodes: manifest.nodes,
        users: manifest.users
      };
      
      return exportData;
    } catch (error) {
      console.error('Error exporting for federation:', error);
      return null;
    }
  }

  /**
   * Import storage from federation
   */
  async importFromFederation(exportData) {
    try {
      if (!exportData || !exportData.contributions) {
        throw new Error('Invalid export data');
      }

      let importedCount = 0;
      for (const [hash, info] of Object.entries(exportData.contributions)) {
        // Check if we already have this contribution
        try {
          await this.getContribution(hash);
        } catch {
          // Contribution doesn't exist, import it
          const contribution = await this.getContribution(hash);
          if (contribution) {
            await this.storeContribution(contribution);
            importedCount++;
          }
        }
      }

      return { success: true, importedCount };
    } catch (error) {
      console.error('Error importing from federation:', error);
      return { success: false, error: error.message };
    }
  }
}

export default ContentAddressedStorage;
