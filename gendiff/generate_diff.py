import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1:
        data1 = json.load(file1)

    with open(file_path2) as file2:
        data2 = json.load(file2)

    keys = sorted(set(data1) | set(data2))
    lines = [build_line(key, data1, data2) for key in keys]

    return "{\n" + "\n".join(lines) + "\n}"


def build_line(key, data1, data2):
    if key not in data2:
        return "  - {0}: {1}".format(key, stringify(data1[key]))
    if key not in data1:
        return "  + {0}: {1}".format(key, stringify(data2[key]))
    if data1[key] == data2[key]:
        return "    {0}: {1}".format(key, stringify(data1[key]))
    old_line = "  - {0}: {1}".format(key, stringify(data1[key]))
    new_line = "  + {0}: {1}".format(key, stringify(data2[key]))
    return "{0}\n{1}".format(old_line, new_line)


def stringify(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)