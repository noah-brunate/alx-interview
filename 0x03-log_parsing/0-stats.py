#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""

import sys


status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
count = 0


try:
    for line in sys.stdin:
        arg_list = line.split(" ")

    if len(arg_list) > 4:
        size = int(arg_list[-1])
        status = arg_list[-2]

        if status in status_dict.keys():
            status_dict[status] += 1

        file_size += size
        count += 1
    if count == 10:
        count = 0
        print(f"File size: {file_size}")
        for key, val in sorted(status_dict.items()):
            if val != 0:
                print(f"{key}: {val}")

except Exception as e:
    pass
finally:
    print(f"File size: {file_size}")
    for key, val in sorted(status_dict.items()):
        if val != 0:
            print(f"{key}: {val}")
