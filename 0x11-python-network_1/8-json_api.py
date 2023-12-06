#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""
import requests
import sys

if __name__ == '__main__':

    try:
        par = {'q': sys.argv[1]}
    except:
        par = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=par)
    try:
        res = r.json()
        if res == {}:
            print('No result')
        else:
            print('[{}]: {}'.format(res.get('id'), res.get('name')))
    except:
        print('Not a valid JSON')
