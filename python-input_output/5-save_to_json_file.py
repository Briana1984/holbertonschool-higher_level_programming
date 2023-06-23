#!/usr/bin/python3
"""
writes an Object using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    convert the object
    """
    with open(filename, 'w+', encoding="utf-8") as f:
        object = json.dumps(my_obj)
        f.write(object)
