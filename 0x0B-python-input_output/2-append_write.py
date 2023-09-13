#!/usr/bin/python3
"""only on function append_write"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
        

