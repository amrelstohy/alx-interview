#!/usr/bin/python3
import sys
import re
import signal

total_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


def print_metrics():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))


signal.signal(signal.SIGINT, signal_handler)

log_entry_regex = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.+?)\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)'
)

lines_count = 0

for line in sys.stdin:
    match = re.match(log_entry_regex, line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        total_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        lines_count += 1

        if lines_count % 10 == 0:
            print_metrics()

print_metrics()
