#!/usr/bin/python3
"""5-text_indentation"""


def text_indentation(text):
    """Print with indentation"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    line = None
    for ch in text:
        if line is None:
            line = ""
        line += ch
        if ch in '.:?':
            print(line.strip())
            print()
            line = None
    if line is not None:
        print(line.strip())
