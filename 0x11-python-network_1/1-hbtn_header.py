#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import urllib.request
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        headers = res.headers
        print(headers['X-Request-Id'])
