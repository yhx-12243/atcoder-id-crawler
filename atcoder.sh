#!/bin/bash

if [ $# -eq 0 ]
then exit 1
fi

if ! ./atcoder_list.py
then exit 2
fi

./atcoder_crawler.py $1
./atcoder_compress.py
./final_compress.js

rm *.tmp
