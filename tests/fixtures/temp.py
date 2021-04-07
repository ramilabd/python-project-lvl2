from sys import path
path.insert(0, path[0] + '/../')
from gendiff.scripts.gendiff import generate_diff, stylish
from pprint import pprint

# [print(_) for _ in path]

file_path1 = './files_for_testing/file_1.json'
file_path2 = './files_for_testing/file_2.json'


pprint(generate_diff(file_path1, file_path2), sort_dicts=False, indent=2)
stylish(generate_diff(file_path1, file_path2))

# {
#     host: hexlet.io
#   - timeout: 50
#   + timeout: 20
#   - proxy: 123.234.53.22
#   - follow: false
#   + verbose: true
# }