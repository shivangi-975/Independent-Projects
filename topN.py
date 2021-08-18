#!/usr/bin/env python
# Reducer that returns the top N results per keyword
import sys

maxN = int(sys.argv[1])
last_key = None
count = 0
for line in sys.stdin:
    (key, value) = line.strip().split("\t", 1)
    if key != last_key:
        count = 0
        last_key = key;
    if count < maxN:
        print "%s\t%s" % (key, value)
    count += 1
