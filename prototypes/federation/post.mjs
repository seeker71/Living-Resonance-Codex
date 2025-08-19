#!/usr/bin/env node
import http from 'http';

function postActivity(activity) {
	return new Promise((resolve, reject) => {
		const data = Buffer.from(JSON.stringify(activity));
		const req = http.request({
			host: 'localhost',
			port: 8787,
			path: '/inbox',
			method: 'POST',
			headers: {
				'Content-Type': 'application/activity+json',
				'Content-Length': data.length
			}
		}, (res) => {
			let body = '';
			res.on('data', chunk => body += chunk);
			res.on('end', () => resolve({ statusCode: res.statusCode, body }));
		});
		req.on('error', reject);
		req.write(data);
		req.end();
	});
}

async function main() {
	const base = {
		type: 'Create',
		actor: 'codex@localhost',
		object: {
			type: 'Contribution',
			nodeId: 'codex:Field',
			content: 'Field refinement via breath',
			resonance: 0.72
		}
	};

	const activity2 = {
		...base,
		object: {
			...base.object,
			nodeId: 'codex:Breath',
			content: 'Adding breath node insight',
			resonance: 0.68
		}
	};

	console.log('Posting activity 1...');
	const r1 = await postActivity(base);
	console.log(' ->', r1.statusCode, r1.body || '');

	console.log('Posting activity 2...');
	const r2 = await postActivity(activity2);
	console.log(' ->', r2.statusCode, r2.body || '');
}

main().catch((e) => { console.error('Error posting activities:', e); process.exit(1); });
