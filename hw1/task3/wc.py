import sys


def wc(file_name):
    try:
        with open(file_name, 'r') as file:
            num_lines, num_words, num_bytes = 0, 0, 0

            for line in file:
                num_lines += 1
                num_words += len(line.split())
                num_bytes += len(line.encode('utf-8'))

            return num_lines, num_words, num_bytes, None
    except FileNotFoundError:
        print(f"wc: {file_name}: No such file or directory")
        return 0, 0, 0, FileNotFoundError


if __name__ == "__main__":
    total_lines, total_words, total_bytes = 0, 0, 0

    for i, file_name in enumerate(sys.argv[1:]):
        num_lines, num_words, num_bytes, err = wc(file_name)
        if err == FileNotFoundError:
            if i == 0:
                exit(1)
            else:
                continue

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
        print(f"{num_lines}\t{num_words}\t{num_bytes}\t{file_name}")

    print(f"{total_lines}\t{total_words}\t{total_bytes}\ttotal")
