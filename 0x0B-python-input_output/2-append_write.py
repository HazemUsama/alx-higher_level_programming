#!/usr/bin/python3
"""only on function append_write"""


def append_write(filename="", text=""):
    """
    Append a string to the end of the file
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
