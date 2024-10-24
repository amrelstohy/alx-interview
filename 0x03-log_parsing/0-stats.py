#!/usr/bin/python3
"""Module"""
import re
import sys

log_pattern = re.compile(
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (200|301|400|401|403|404|405|500) (\d+)'
)

total_size = 0
status_count = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            file_size = int(match.group(4))
            status_code = int(match.group(3))

            total_size += file_size
            status_count[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_count):
                    if status_count[code] > 0:
                        print("{}: {}".format(code, status_count[code]))

except KeyboardInterrupt:
    print("\nFile size: {}".format(total_size))
    for code in sorted(status_count):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))
