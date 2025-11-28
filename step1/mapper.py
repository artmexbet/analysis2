#!/usr/bin/env python3
"""
Step 1 Mapper: Parses log lines and emits (user, request_type) pairs.

Input: Log lines in format:
    IP - Username [timestamp] METHOD /path status size referrer

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
        username = parts[2]
        method = parts[4]
        path = parts[5]
        request_type = f"{method} {path}"
        print(f"{username}\t{request_type}")
    except (IndexError, ValueError):
        continue
