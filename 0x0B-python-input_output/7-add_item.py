#!/usr/bin/python3
"""script that adds all arguments to a Python list,
    and then save them to a file"""
import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = 'add_item.json'

if os.path.exists(file_name):
    items = load_from_json_file(file_name)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, file_name)
