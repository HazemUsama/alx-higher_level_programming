#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':

    with requests.get('https://alx-intranet.hbtn.io/status') as res:
        html = res.text
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
