#!/usr/bin/env node

fs = require('fs');
rd = require('./deflate/rawdeflate').RawDeflate.deflate;

raw = fs.readFileSync('compressed.tmp', 'utf-8')
A = Array.apply(null, {length : 10}).map((x, i) => rd(raw, i).length);
idx = A.indexOf(Math.min.apply(null, A))
c = rd(raw, idx)
c = Buffer.from(c, 'binary').toString('base64')
fs.writeFileSync('base64_result', c)
