#!/usr/bin/env python3
"""
Step 2 Mapper: Passes through the data from Step 1.

Input: tab-separated:
    Username\tMETHOD /path\tcount

Output: tab-separated (count as key for sorting):
    count\tUsername\tMETHOD /path
"""
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        parts = line.split('\t')
        username = parts[0]
        request = parts[1]
        count = int(parts[2])
        print(f"{count}\t{username}\t{request}")
    except (IndexError, ValueError):
        continue
