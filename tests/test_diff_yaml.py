# -*- coding:utf-8 -*-

"""Testing the difference calculation of json files."""

from gendiff.generate_diff import gen_diff


correct_diff = """
{
    host: hexlet.io
  - timeout: 50
  + timeout: 20
  - proxy: 123.234.53.22
  - follow: False
  + verbose: True
}
"""

def test_gen_diff_yaml():
    file_path1 = './tests/fixtures/file_1.yaml'
    file_path2 = './tests/fixtures/file_2.yaml'
    assert gen_diff(file_path1, file_path2) == correct_diff
