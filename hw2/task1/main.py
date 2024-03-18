from latex_gen import generate_latex_table


def main():
    print(generate_latex_table([
        [1, 2, 3],
        ["a", "b", "c"],
        [4, 5, 6],
    ]))


if __name__ == "__main__":
    main()