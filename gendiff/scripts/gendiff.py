# -*- coding:utf-8 -*-

"""Gendiff script module."""


from gendiff.cli import run
from gendiff.generate_diff import gen_diff, show_diff


def main():
    """Program start."""
    args = run()
    show_diff(gen_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
