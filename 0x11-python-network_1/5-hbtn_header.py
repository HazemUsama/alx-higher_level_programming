#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    headers = requests.get(url).headers
    print(headers.get('X-Request-Id'))
