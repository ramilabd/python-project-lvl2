from gendiff import generate_diff
from gendiff.cli import run


def main():
    args = run()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()