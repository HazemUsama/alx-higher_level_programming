#!/usr/bin/python3
"""5-text_indentation"""


def text_indentation(text):
    """Print with indentation"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for ch in text.strip():
        print(ch, end='')
        if ch in '.?:':
            print('\n')
