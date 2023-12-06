#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""
import requests
import sys

if __name__ == '__main__':

    try:
        par = {'q': sys.argv[1]}
    except:
        par = ""

    res = requests.post('http://httpbin.org/post', params=par).json()
    if not isinstance(res, dict):
        print('Not a valid JSON')
    elif res == {}:
        print('No result')
    else:
        print('[{}]: {}'.format(res['id'], res['name']))
