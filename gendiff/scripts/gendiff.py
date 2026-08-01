import json

from gendiff.cli import run


def main():
    args = run()

    with open(args.first_file) as file1:
        data1 = json.load(file1)

    with open(args.second_file) as file2:
        data2 = json.load(file2)

    print(data1)
    print(data2)


if __name__ == "__main__":
    main()