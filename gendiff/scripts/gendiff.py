from gendiff.cli import run
from gendiff import generate_diff


def main():
    args = run()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()