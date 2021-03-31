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
    diff_line = '  {0} {1}: {2}'

    for key, value in file1.items():
        if (key, value) in file2.items():
            diff.append(diff_line.format(' ', key, value))
        elif key in file2 and value != file2[key]:
            diff.append(diff_line.format('-', key, file1.get(key)))
            diff.append(diff_line.format('+', key, file2.get(key)))

    for key in file1.keys():
        if key not in file2.keys():
            diff.append(diff_line.format('-', key, str(file1.get(key)).lower()))

    for key in file2.keys() - file1.keys():
        diff.append(diff_line.format('+', key, str(file2.get(key)).lower()))

    return '\n{0}\n{1}\n{2}\n'.format('{', '\n'.join(diff), '}')


if __name__ == '__main__':
    main()
