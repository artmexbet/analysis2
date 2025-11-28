#!/usr/bin/env python3
"""
Step 2 Reducer: Finds top 4 users with maximum identical requests.

Input: tab-separated (sorted by count in descending order):
    count\tUsername\tMETHOD /path

Output: Top 4 results:
    Username\tMETHOD /path\tcount

Note: Input is expected to be sorted by count descending, so we can
process records sequentially and stop after 4 results.
"""
import sys

count_output = 0

for line in sys.stdin:
    if count_output >= 4:
        break
        
    line = line.strip()
    if not line:
        continue
    
    try:
        parts = line.split('\t')
        count = int(parts[0])
        username = parts[1]
        request = parts[2]
        print(f"{username}\t{request}\t{count}")
        count_output += 1
    except (IndexError, ValueError):
        continue
