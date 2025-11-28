#!/usr/bin/env python3
"""
Step 2 Reducer: Finds top 4 users with maximum identical requests.

Input: tab-separated (sorted by count):
    count\tUsername\tMETHOD /path

Output: Top 4 results:
    Username\tMETHOD /path\tcount
"""
import sys

results = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        parts = line.split('\t')
        count = int(parts[0])
        username = parts[1]
        request_type = parts[2]
        results.append((count, username, request_type))
    except (IndexError, ValueError):
        continue

results.sort(key=lambda x: -x[0])

for count, username, request_type in results[:4]:
    print(f"{username}\t{request_type}\t{count}")
