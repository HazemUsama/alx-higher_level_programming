#!/usr/bin/python3
"""display your github id"""
import requests
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    print(r.json().get('id'))
