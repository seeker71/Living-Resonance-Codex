#!/usr/bin/env node
import http from 'http';
import url from 'url';
import ContentAddressedStorage from './content-storage.js';

const port = process.env.PORT || 8787;

// Initialize content-addressed storage
const storage = new ContentAddressedStorage('./federation-storage');

const routes = {
  '/.well-known/webfinger': (_req, res) => {
    res.writeHead(200, {'Content-Type':'application/json'});
    res.end(JSON.stringify({
      subject: "acct:codex@localhost",
      links: [
        {
          rel: "self",
          type: "application/activity+json",
          href: "http://localhost:8787/actor"
        },
        {
          rel: "http://www.w3.org/ns/activitystreams#inbox",
          type: "application/activity+json",
          href: "http://localhost:8787/inbox"
        },
        {
          rel: "http://www.w3.org/ns/activitystreams#outbox",
          type: "application/activity+json",
          href: "http://localhost:8787/outbox"
        }
      ]
    }));
  },

  '/actor': (_req, res) => {
    res.writeHead(200, {'Content-Type':'application/activity+json'});
    res.end(JSON.stringify({
      "@context": ["https://www.w3.org/ns/activitystreams"],
      "id": "http://localhost:8787/actor",
      "type": "Person",
      "name": "Living Codex Federation Node",
      "inbox": "http://localhost:8787/inbox",
      "outbox": "http://localhost:8787/outbox",
      "preferredUsername": "codex",
      "summary": "A federated node of the Living Resonance Codex"
    }));
  },

  '/inbox': async (req, res) => {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      try {
        const activity = JSON.parse(body || '{}');
        console.log('INBOX activity', activity);

        // Handle different activity types
        if (activity.type === 'Create' && activity.object) {
          // Store contribution in content-addressed storage
          const contribution = {
            nodeId: activity.object.nodeId || 'unknown',
            userId: activity.actor || 'anonymous',
            type: activity.object.type || 'contribution',
            content: activity.object.content,
            resonance: activity.object.resonance || 0.5,
            timestamp: activity.published || new Date().toISOString()
          };

          const result = await storage.storeContribution(contribution);
          console.log('Stored contribution:', result);
        }

        res.writeHead(202);
        res.end();
      } catch(e) {
        console.error('Error processing inbox activity:', e);
        res.writeHead(400);
        res.end('bad json');
      }
    });
  },

  '/outbox': async (_req, res) => {
    try {
      const manifest = await storage.loadManifest();
      const recentContributions = Object.values(manifest.contributions)
        .sort((a, b) => new Date(b.storedAt) - new Date(a.storedAt))
        .slice(0, 20);

      res.writeHead(200, {'Content-Type':'application/activity+json'});
      res.end(JSON.stringify({
        "@context": ["https://www.w3.org/ns/activitystreams"],
        "id": "http://localhost:8787/outbox",
        "type": "OrderedCollection",
        "totalItems": Object.keys(manifest.contributions).length,
        "orderedItems": recentContributions.map(contrib => ({
          type: "Create",
          actor: "http://localhost:8787/actor",
          object: {
            type: "Contribution",
            nodeId: contrib.nodeId,
            userId: contrib.userId,
            contributionType: contrib.type,
            storedAt: contrib.storedAt,
            size: contrib.size
          }
        }))
      }));
    } catch (error) {
      console.error('Error getting outbox:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  },

  // Phase 4: Content-addressed storage endpoints
  '/contributions/:hash': async (req, res) => {
    try {
      const hash = req.url.split('/').pop();
      const contribution = await storage.getContribution(hash);
      
      if (contribution) {
        res.writeHead(200, {'Content-Type':'application/json'});
        res.end(JSON.stringify(contribution));
      } else {
        res.writeHead(404);
        res.end('Contribution not found');
      }
    } catch (error) {
      console.error('Error getting contribution:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  },

  '/contributions/node/:nodeId': async (req, res) => {
    try {
      const nodeId = req.url.split('/').pop();
      const contributions = await storage.getNodeContributions(nodeId);
      
      res.writeHead(200, {'Content-Type':'application/json'});
      res.end(JSON.stringify({
        nodeId,
        contributions,
        count: contributions.length
      }));
    } catch (error) {
      console.error('Error getting node contributions:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  },

  '/contributions/user/:userId': async (req, res) => {
    try {
      const userId = req.url.split('/').pop();
      const contributions = await storage.getUserContributions(userId);
      
      res.writeHead(200, {'Content-Type':'application/json'});
      res.end(JSON.stringify({
        userId,
        contributions,
        count: contributions.length
      }));
    } catch (error) {
      console.error('Error getting user contributions:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  },

  '/storage/stats': async (_req, res) => {
    try {
      const stats = await storage.getStorageStats();
      
      res.writeHead(200, {'Content-Type':'application/json'});
      res.end(JSON.stringify(stats));
    } catch (error) {
      console.error('Error getting storage stats:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  },

  '/storage/export': async (_req, res) => {
    try {
      const exportData = await storage.exportForFederation();
      
      res.writeHead(200, {'Content-Type':'application/json'});
      res.end(JSON.stringify(exportData));
    } catch (error) {
      console.error('Error exporting storage:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  },

  '/storage/import': async (req, res) => {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      try {
        const exportData = JSON.parse(body || '{}');
        const result = await storage.importFromFederation(exportData);
        
        res.writeHead(200, {'Content-Type':'application/json'});
        res.end(JSON.stringify(result));
      } catch (error) {
        console.error('Error importing storage:', error);
        res.writeHead(400);
        res.end('Invalid import data');
      }
    });
  },

  // Phase 4: Federation discovery endpoints
  '/federation/peers': (_req, res) => {
    res.writeHead(200, {'Content-Type':'application/json'});
    res.end(JSON.stringify({
      peers: [
        {
          domain: "localhost:8787",
          name: "Living Codex Federation Node",
          inbox: "http://localhost:8787/inbox",
          outbox: "http://localhost:8787/outbox",
          lastSeen: new Date().toISOString()
        }
      ]
    }));
  },

  '/federation/sync': async (_req, res) => {
    try {
      // This would implement cross-instance synchronization
      // For now, return current state
      const manifest = await storage.loadManifest();
      
      res.writeHead(200, {'Content-Type':'application/json'});
      res.end(JSON.stringify({
        synced: true,
        timestamp: new Date().toISOString(),
        nodeCount: Object.keys(manifest.nodes).length,
        contributionCount: Object.keys(manifest.contributions).length
      }));
    } catch (error) {
      console.error('Error during federation sync:', error);
      res.writeHead(500);
      res.end('Internal server error');
    }
  }
};

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url);
  const path = parsedUrl.pathname;
  
  // Handle dynamic routes
  if (path.startsWith('/contributions/') && path.split('/').length === 3) {
    const hash = path.split('/')[2];
    if (hash && hash.length === 64) { // SHA-256 hash length
      return routes['/contributions/:hash'](req, res);
    }
  }
  
  if (path.startsWith('/contributions/node/')) {
    return routes['/contributions/node/:nodeId'](req, res);
  }
  
  if (path.startsWith('/contributions/user/')) {
    return routes['/contributions/user/:userId'](req, res);
  }
  
  const handler = routes[path];
  return handler ? handler(req, res) : (res.writeHead(404), res.end('not found'));
});

server.listen(port, () => {
  console.log('🌊 Living Codex Federation Server (Phase 4) listening on http://localhost:' + port);
  console.log('📚 Content-addressed storage initialized');
  console.log('🔗 Federation endpoints available:');
  console.log('   - /.well-known/webfinger');
  console.log('   - /actor');
  console.log('   - /inbox /outbox');
  console.log('   - /contributions/*');
  console.log('   - /storage/*');
  console.log('   - /federation/*');
});