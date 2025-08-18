#!/usr/bin/env node
import http from 'http';
import url from 'url';

const port = process.env.PORT || 8787;

const routes = {
  '/.well-known/webfinger': (_req, res) => {
    res.writeHead(200, {'Content-Type':'application/json'});
    res.end(JSON.stringify({subject:"acct:codex@localhost", links:[]}));
  },
  '/inbox': async (req, res) => {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', ()=>{
      try {
        const activity = JSON.parse(body||'{}');
        console.log('INBOX activity', activity);
        res.writeHead(202); res.end();
      } catch(e){ res.writeHead(400); res.end('bad json'); }
    });
  },
  '/outbox': (_req, res) => {
    res.writeHead(200, {'Content-Type':'application/json'});
    res.end(JSON.stringify({items:[]}));
  }
};

const server = http.createServer((req, res) => {
  const path = url.parse(req.url).pathname;
  const handler = routes[path];
  return handler ? handler(req,res) : (res.writeHead(404), res.end('not found'));
});

server.listen(port, ()=> console.log('Federation stub listening on http://localhost:'+port));