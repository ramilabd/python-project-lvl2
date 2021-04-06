# -*- coding:utf-8 -*-

"""Opening and reading files."""


import json


def read_file(file_path):
    """Read files.

    Args:
        file_path (str): path to file

    Returns:
        (dict) : file object
    """
    with open(file_path, 'r', encoding='utf-8') as file_object:
        file = json.load(file_object)
    return file
