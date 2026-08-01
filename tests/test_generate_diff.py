from gendiff import generate_diff


def test_generate_diff_flat_json():
    with open('tests/test_data/expected_flat_stylish.txt') as file:
        expected = file.read()

    actual = generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json',
    )
    assert actual == expected.rstrip('\n')