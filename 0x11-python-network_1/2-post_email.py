#!/usr/bin/python3
"""sends a POST request to the passed URL"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    values = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, values)
    with urllib.request.urlopen(req) as res:
        print(res.read().deconde('utf-8'))
