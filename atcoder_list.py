#!/usr/bin/env python

import sys, json, requests

ac = {}

print('Crawling full list ...', file = sys.stderr)

r = requests.post('https://vjudge.net/problem/data', {
		'category' : 'all',
		'length' : 23333,
		'OJId' : 'AtCoder'
	})

if not r.ok:
	print('Crawling failed, please retry.', file = sys.stderr)
	sys.exit(1)

for e in r.json()['data']:
	ac[e['originProb']] = e['id']

with open('atcoder.tmp', 'w') as f:
	json.dump(ac, f)

print('Flushing finished.', file = sys.stderr)
