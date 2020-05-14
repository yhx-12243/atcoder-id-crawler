#!/usr/bin/env python

import re, sys, json, asyncio, aiohttp

assert len(sys.argv) > 1 and sys.argv[1].isdigit()
limit = int(sys.argv[1])

ptrn = r'http[s]?://([\w-]+).contest.atcoder.jp/tasks/([\w-]+)\?lang=en'

result_dict = {}
fetched = 0

async def fetch(id, url):
	global fetched
	try:
		TLE = aiohttp.ClientTimeout(10)
		async with aiohttp.ClientSession(timeout = TLE) as session:
			async with session.head(url) as r:
				Loc = r.headers['Location']
				res = re.match(ptrn, Loc)
				if res:
					Loc = 'https://atcoder.jp/contests/{}/tasks/{}'.format(res[1], res[2])
					result_dict[id] = Loc
					print('Fetched {} (result = {})'.format(id, Loc), file = sys.stderr)
				else:
					print('Fetched {} (unrecognized result = {})'.format(id, Loc), file = sys.stderr)
				fetched += 1
	except:
		pass

with open('atcoder.tmp') as f:
	ac = json.load(f)

with open('result.txt') as f:
	for line in f.readlines():
		u, v = line.split()
		result_dict[int(u)] = v

L = asyncio.get_event_loop()

while True:
	coroutines = []
	fetched = count = 0

	for u, v in ac.items():
		if not u.isdigit():
			continue
		u = int(u)
		if u not in result_dict:
			print('Attempt {} (vjudge id = {}) : Accessing ...'.format(u, v), file = sys.stderr)
			coroutines.append(fetch(int(u), 'https://vjudge.net/problem/{}/origin'.format(v)))
			count += 1
			if count >= limit:
				break

	L.run_until_complete(asyncio.gather(*coroutines))
	print('=' * 16, file = sys.stderr)
	pp = 'Total fetched : {}/{}, continue ? '.format(fetched, count)
	resp = input(pp)
	while resp == '':
		resp = input(pp)
	if resp.upper() != 'Y':
		break

L.close()

with open('result.txt', 'w') as f:
	for u, v in sorted(result_dict.items()):
		print(u, v, file = f)
