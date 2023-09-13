#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read and print file to stdout"""
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line)
