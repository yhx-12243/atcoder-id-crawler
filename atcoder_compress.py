#!/usr/bin/env python

import re

ptrn = r'http[s]?://atcoder\.jp/contests/([\w-]+)/tasks/([\w-]+)'

a = ['']
C1 = C2 = 0
charset = set()

with open('result.txt') as f:
	for line in f.readlines():
		u, v = line.split()
		res = re.match(ptrn, v)
		if res:
			if res[2].startswith(res[1]) and res[2][len(res[1])] == '_':
				r = res[1] + '>' + res[2][len(res[1]) + 1:]
			else:
				r = res[1] + '#' + res[2]
			u = int(u)
			while u >= len(a):
				a.extend([''] * len(a))
			a[u] = r
			charset.update(set(res[1]))
			charset.update(set(res[2]))

result_str = '|'.join(a).rstrip('|')

with open('compressed.tmp', 'w') as f:
	print(result_str, file = f)
