#!/usr/bin/env python3
import sys

rows = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if '\t' not in line:
        continue
    key, value = line.split('\t', 1)
    rows.append((key, value))

rows.sort(key=lambda x: x[0])

for key, value in rows:
    print(f"{key}\t{value}")
