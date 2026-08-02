from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def format_diff(diff, format_name='stylish'):
    formatter = FORMATTERS[format_name]
    return formatter(diff)