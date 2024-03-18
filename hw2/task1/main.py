import latex_gen as tex


def main():
    print(tex.generate_latex_table([
        [1, 2, 3],
        ["a", "b", "c"],
        [4, 5, 6],
    ]))

    print(tex.generate_latex_image("image"))


if __name__ == "__main__":
    main()