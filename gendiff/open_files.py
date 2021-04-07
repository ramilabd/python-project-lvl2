# -*- coding:utf-8 -*-

"""Opening and reading files."""

import json
import os

import yaml


def read_file(file_path):
    """Read files.

    Args:
        file_path (str): path to file

    Returns:
        (dict) : file object
    """
    file_extension = os.path.splitext(file_path)[-1]

    if file_extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as file_object:
            file = json.load(file_object)
        return file
    elif file_extension in {'.yaml', '.yml'}:
        with open(file_path, 'r', encoding='utf-8') as file_obejct:
            file = yaml.safe_load(file_obejct)
        return file
