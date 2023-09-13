#!/usr/bin/python3
"""Write to a file"""


def read_file(filename=""):
    """Write to the file"""
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)
