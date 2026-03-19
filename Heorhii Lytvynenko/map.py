#!/usr/bin/env python3
import sys


def parse_stop(raw_stop: str):
    """Parse one stop block like {k=v}{k=v}... into dict."""
    data = {}
    parts = raw_stop.split('}{')
    for part in parts:
        if '=' not in part:
            continue
        key, value = part.split('=', 1)
        key = key.strip('{} ')
        value = value.strip('{} ')
        data[key] = value
    return data


def emit_from_line(line: str):
    line = line.strip()
    if not line:
        return

    # Each line can contain multiple records: {{...}}{{...}}{{...}}
    trimmed = line
    if trimmed.startswith('{{'):
        trimmed = trimmed[2:]
    if trimmed.endswith('}}'):
        trimmed = trimmed[:-2]

    stops = trimmed.split('}}{{')

    for stop in stops:
        row = parse_stop(stop)

        zona = row.get('geografine zona')
        diena = row.get('sustojimo savaites diena')
        siuntos = row.get('siuntu skaicius')
        klientai = row.get('Sustojimo klientu skaicius')

        # Zone/day/packages are required for grouping and parcel totals.
        # Customer count is optional: if missing, count it as 0 and keep the record.
        if not (zona and diena and siuntos):
            continue

        try:
            siuntos_i = int(float(siuntos))
            klientai_i = int(float(klientai)) if klientai not in (None, "") else 0
        except ValueError:
            continue

        # key = zona|diena, value = siuntos,klientai
        print(f"{zona}|{diena}\t{siuntos_i},{klientai_i}")


for input_line in sys.stdin:
    emit_from_line(input_line)
