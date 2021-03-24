# -*- coding:utf-8 -*-

"""Gendiff script module."""

import argparse
import json


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


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


if __name__ == '__main__':
    main()
