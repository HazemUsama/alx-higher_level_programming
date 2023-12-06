#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""
import urllib.request
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.status))
     

