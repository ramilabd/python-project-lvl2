# -*- coding:utf-8 -*-

"""
The module contains the generate_diff function.

Function generate_iff returns the difference in the files
"""

import json


def generate_diff(file_path1, file_path2):
    """Calculate the difference between two files.

    Args:
        file_path1 (str): path to first file
        file_path2 (str): path to second file

    Returns:
        str: diff
    """
    with open(file_path1, 'r', encoding='utf-8') as file_object1:
        file1 = json.load(file_object1)
        with open(file_path2, 'r', encoding='utf-8') as file_object2:
            file2 = json.load(file_object2)

    diff = []

    keys_file1 = set(file1.keys())
    keys_file2 = set(file2.keys())
    result_str = '  {0} {1}: {2}'

    for key in keys_file1 - keys_file2:
        diff.append(result_str.format('-', key, file1.get(key)))

    for key in keys_file2 - keys_file1:
        diff.append(result_str.format('+', key, file2.get(key)))

    for key in keys_file1 & keys_file2:
        if file1.get(key) == file2.get(key):
            diff.append(result_str.format(' ', key, file1.get(key)))
        else:
            diff.append(result_str.format('-', key, file1.get(key)))
            diff.append(result_str.format('+', key, file2.get(key)))

    return '{0}\n{1}\n{2}'.format('{', '\n'.join(diff), '}')
