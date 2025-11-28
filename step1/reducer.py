#!/usr/bin/env python3
"""
Step 1 Reducer: Counts identical requests per user.

Input: tab-separated key-value pairs (sorted by key):
    Username\tMETHOD /path

Output: tab-separated:
    Username\tMETHOD /path\tcount
"""
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        parts = line.split('\t')
        username = parts[0]
        request_type = parts[1]
        key = f"{username}\t{request_type}"
    except (IndexError, ValueError):
        continue
    
    if current_key == key:
        current_count += 1
    else:
        if current_key is not None:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = 1

if current_key is not None:
    print(f"{current_key}\t{current_count}")
