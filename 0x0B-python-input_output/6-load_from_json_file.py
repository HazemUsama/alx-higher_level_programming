#!/usr/bin/python3
"""one function load_from_json_file"""
import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
