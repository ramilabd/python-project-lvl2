#!/usr/bin/env python3

import argparse


def run():
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
    return args
