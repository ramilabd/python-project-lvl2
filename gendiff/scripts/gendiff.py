from gendiff import generate_diff
from gendiff.scripts.cli import run


def main():
    args = run()
    format_name = args.format or 'stylish'
    print(generate_diff(args.first_file, args.second_file, format_name))


if __name__ == "__main__":
    main()