#!/usr/bin/python3
"""5-text_indentation"""


def text_indentation(text):
    """Print with indentation"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    line = ""
    for ch in text:
        line += ch
        if ch in '.:?':
            print(line.strip())
            print()
            line = ""
    if line != "":
        print(line.strip())
