from io import TextIOWrapper
import sys

def tail(file: TextIOWrapper, num_lines=10):
    lines = file.readlines()
    num_lines = min(num_lines, len(lines))
    start_index = len(lines) - num_lines
    for line in lines[start_index:]:
        print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        tail(sys.stdin)
    elif len(sys.argv) >= 2:
        for file_name in sys.argv[1:]:
            try:
                with open(file_name, 'r') as file:
                    if len(sys.argv) > 2:
                        print(f"==> {file_name} <==")
                    tail(file)
            except FileNotFoundError:
                print(f"tail: cannot open '{file_name}' for reading: No such file or directory")
                sys.exit(1)
