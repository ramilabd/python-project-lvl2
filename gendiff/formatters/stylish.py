INDENT_SIZE = 4
SIGN_OFFSET = 2


def format_stylish(diff):
    return "{\n" + render_nodes(diff, 1) + "\n}"


def render_nodes(nodes, depth):
    lines = [render_node(node, depth) for node in nodes]
    return "\n".join(lines)


def render_node(node, depth):
    indent = " " * (depth * INDENT_SIZE - SIGN_OFFSET)
    key = node['key']
    node_type = node['type']

    if node_type == 'nested':
        closing_indent = " " * (depth * INDENT_SIZE)
        children = render_nodes(node['children'], depth + 1)
        return f"{indent}  {key}: {{\n{children}\n{closing_indent}}}"

    if node_type == 'added':
        return f"{indent}+ {key}: {stringify(node['value'], depth)}"

    if node_type == 'removed':
        return f"{indent}- {key}: {stringify(node['value'], depth)}"

    if node_type == 'unchanged':
        return f"{indent}  {key}: {stringify(node['value'], depth)}"

    old_value = stringify(node['old_value'], depth)
    new_value = stringify(node['new_value'], depth)
    return f"{indent}- {key}: {old_value}\n{indent}+ {key}: {new_value}"


def stringify(value, depth):
    if isinstance(value, dict):
        return stringify_dict(value, depth)
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def stringify_dict(value, depth):
    indent = " " * ((depth + 1) * INDENT_SIZE)
    closing_indent = " " * (depth * INDENT_SIZE)
    lines = [
        f"{indent}{k}: {stringify(v, depth + 1)}"
        for k, v in value.items()
    ]
    return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
