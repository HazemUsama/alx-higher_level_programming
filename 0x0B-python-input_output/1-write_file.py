#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write to the file"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)

