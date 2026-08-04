def format_plain(diff):
    lines = render_nodes(diff, '')
    return '\n'.join(lines)


def render_nodes(nodes, path):
    lines = []
    for node in nodes:
        lines.extend(render_node(node, path))
    return lines


def render_node(node, path):
    key = node['key']
    node_type = node['type']
    full_path = f'{path}.{key}' if path else key

    if node_type == 'nested':
        return render_nodes(node['children'], full_path)

    if node_type == 'added':
        value = stringify(node['value'])
        return [f"Property '{full_path}' was added with value: {value}"]

    if node_type == 'removed':
        return [f"Property '{full_path}' was removed"]

    if node_type == 'changed':
        old_value = stringify(node['old_value'])
        new_value = stringify(node['new_value'])
        return [
            f"Property '{full_path}' was updated. "
            f"From {old_value} to {new_value}",
        ]

    return []


def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)
