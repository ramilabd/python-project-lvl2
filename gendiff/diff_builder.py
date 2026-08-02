def build_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    return [build_node(key, data1, data2) for key in keys]


def build_node(key, data1, data2):
    if key not in data2:
        return {'key': key, 'type': 'removed', 'value': data1[key]}
    if key not in data1:
        return {'key': key, 'type': 'added', 'value': data2[key]}

    value1, value2 = data1[key], data2[key]

    if isinstance(value1, dict) and isinstance(value2, dict):
        children = build_diff(value1, value2)
        return {'key': key, 'type': 'nested', 'children': children}

    if value1 == value2:
        return {'key': key, 'type': 'unchanged', 'value': value1}

    return {
        'key': key,
        'type': 'changed',
        'old_value': value1,
        'new_value': value2,
    }
