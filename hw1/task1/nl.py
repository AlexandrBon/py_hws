import sys


line_number = 1

def nl(file):
    global line_number
    for line in file:
        print("{:>6}\t{}".format(line_number, line), end='')
        line_number += 1

if __name__ == "__main__":
    if len(sys.argv) == 1:
        nl(sys.stdin)
    elif len(sys.argv) >= 2:
        for file_name in sys.argv[1:]:
            file_name = sys.argv[1]
            try:
                with open(file_name, 'r') as file:
                    nl(file)
            except FileNotFoundError:
                print(f"nl: {file_name}: No such file or directory")
                sys.exit(1)
