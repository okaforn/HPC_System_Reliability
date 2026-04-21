#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:55:19 2026

@author: amakaokafor
"""

import os
import argparse
import csv
from datetime import datetime

def extract_syslog_messages(start_timestamp, end_timestamp, syslog_file, output_file):
    user_time_format = "%Y-%m-%d %H:%M:%S"
    log_time_format = "%Y-%m-%d %H:%M:%S.%f"

    start_dt = datetime.strptime(start_timestamp, user_time_format)
    end_dt = datetime.strptime(end_timestamp, user_time_format)

    written = 0
    read = 0

    with open(syslog_file, newline="") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            read += 1
            if len(row) < 3:
                continue

            try:
                log_dt = datetime.strptime(row[0], log_time_format)
            except ValueError:
                continue

            if start_dt <= log_dt <= end_dt:
                writer.writerow(row)
                written += 1

    print(f"Read {read} lines")
    print(f"Wrote {written} lines")


def main():
    parser = argparse.ArgumentParser(description="Filter syslog CSV by time range")
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-s", "--start", required=True)
    parser.add_argument("-e", "--end", required=True)
    args = parser.parse_args()

    input_file = os.path.expanduser(args.input)
    os.makedirs("output", exist_ok=True)
    output_file = os.path.join("output", os.path.basename(input_file))

    extract_syslog_messages(args.start, args.end, input_file, output_file)

'''usage:
python syslog_extractor.py \
  -i ~/Desktop/aurora_syslog_20240424.csv \
  -s "2024-04-24 10:00:00" \
  -e "2024-04-24 11:00:00"
'''


if __name__ == "__main__":
    main()
