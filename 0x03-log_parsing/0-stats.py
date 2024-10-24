#!/usr/bin/python3
import sys
import re


log_pattern = re.compile(
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (200|301|400|401|403|404|405|500) (\d+)'
)
for line in sys.stdin:
    match = log_pattern.search(line.strip())
    if match:
        print(match)
    else:
        print('oops')

