# -*- coding:utf-8 -*-

"""Difference generator.

The module contains a function that generates the difference between files.
"""

from gendiff.open_files import read_file


def gen_diff(file_path1, file_path2):
    """Calculate the difference between two files.

    Args:
        file_path1 (str): path to first file
        file_path2 (str): path to second file

    Returns:
        str: diff
    """
    file1 = read_file(file_path1)
    file2 = read_file(file_path2)

    diff = []
    str_diff = '{0} {1}: {2}'

    for key in file1.keys():
        if file1.get(key) == file2.get(key):
            diff.append(str_diff.format('   ', key, file1.get(key)))
            file2.pop(key)
        elif file2.get(key, None) is None:
            diff.append(str_diff.format('-', key, file1.get(key)))
        else:
            diff.append(str_diff.format('-', key, file1.get(key)))
            diff.append(str_diff.format('+', key, file2.get(key)))
            file2.pop(key)

    for key in file2.keys():
        diff.append(str_diff.format('+', key, file2.get(key)))

    return '\n{0}\n{1}\n{2}\n'.format('{', '\n  '.join(diff), '}')


def show_diff(diff):
    """Print diff.

    Args:
        diff (str): printed diff to console
    """
    print(diff)
