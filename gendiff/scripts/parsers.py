import json
import os

import yaml


def parse_file(file_path):
    file_extension = os.path.splitext(file_path)[1]

    with open(file_path) as file:
        if file_extension == '.json':
            return json.load(file)
        if file_extension in ('.yml', '.yaml'):
            return yaml.safe_load(file)

    raise ValueError(f'Unsupported file format: {file_extension}')
