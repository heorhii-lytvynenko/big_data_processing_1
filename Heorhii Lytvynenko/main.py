#!/usr/bin/env python3
import subprocess
from pathlib import Path

base = Path(__file__).resolve().parent
input_file = base / 'duom_full.txt'
map_out = base / 'mapout.txt'
sorted_out = base / 'smapout.txt'
red_out = base / 'redout.txt'

with input_file.open('r', encoding='utf-8') as fin, map_out.open('w', encoding='utf-8') as fout:
    subprocess.run(['python', str(base / 'map.py')], stdin=fin, stdout=fout, check=True)

with map_out.open('r', encoding='utf-8') as fin, sorted_out.open('w', encoding='utf-8') as fout:
    subprocess.run(['python', str(base / 'sort.py')], stdin=fin, stdout=fout, check=True)

with sorted_out.open('r', encoding='utf-8') as fin, red_out.open('w', encoding='utf-8') as fout:
    subprocess.run(['python', str(base / 'red.py')], stdin=fin, stdout=fout, check=True)

print(f'Done. Results: {red_out}')
