#!/usr/bin/env python3
import sys

current_key = None
sum_siuntos = 0
sum_klientai = 0

for line in sys.stdin:
    line = line.strip()
    if not line or '\t' not in line:
        continue

    key, payload = line.split('\t', 1)
    if ',' not in payload:
        continue

    siuntos_s, klientai_s = payload.split(',', 1)

    try:
        siuntos = int(siuntos_s)
        klientai = int(klientai_s)
    except ValueError:
        continue

    if key == current_key:
        sum_siuntos += siuntos
        sum_klientai += klientai
    else:
        if current_key is not None:
            print(f"{current_key}\t{sum_siuntos}\t{sum_klientai}")
        current_key = key
        sum_siuntos = siuntos
        sum_klientai = klientai

if current_key is not None:
    print(f"{current_key}\t{sum_siuntos}\t{sum_klientai}")
