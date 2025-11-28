#!/usr/bin/env python3
"""
Step 1 Mapper: Parses log lines and emits (user, request) pairs.

Input: Log lines in format:
    IP - Username [timestamp] METHOD /path status size referrer
    Fields by space: 0=IP, 1=-, 2=Username, 3=[timestamp], 4=METHOD, 5=/path, 6=status, 7=size, 8=referrer

Output: tab-separated key-value pairs:
    Username\tMETHOD /path
"""
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        parts = line.split()
        if len(parts) < 6:
            continue
        username = parts[2]
        method = parts[4]
        path = parts[5]
        request = f"{method} {path}"
        print(f"{username}\t{request}")
    except (IndexError, ValueError):
        continue
