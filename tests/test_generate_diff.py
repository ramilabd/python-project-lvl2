from gendiff import generate_diff


def test_generate_diff_flat_json():
    with open('tests/test_data/expected_flat_stylish.txt') as file:
        expected = file.read()

    actual = generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json',
    )
    assert actual == expected.rstrip('\n')


def test_generate_diff_flat_yaml():
    with open('tests/test_data/expected_flat_stylish.txt') as file:
        expected = file.read()

    actual = generate_diff(
        'tests/test_data/file1.yml',
        'tests/test_data/file2.yml',
    )
    assert actual == expected.rstrip('\n')

def test_generate_diff_nested_json():
    with open('tests/test_data/expected_nested_stylish.txt') as file:
        expected = file.read()

    actual = generate_diff(
        'tests/test_data/nested_file1.json',
        'tests/test_data/nested_file2.json',
    )
    assert actual == expected.rstrip('\n')


def test_generate_diff_nested_yaml():
    with open('tests/test_data/expected_nested_stylish.txt') as file:
        expected = file.read()

    actual = generate_diff(
        'tests/test_data/nested_file1.yml',
        'tests/test_data/nested_file2.yml',
    )
    assert actual == expected.rstrip('\n')