import latex_gen.latex_gen as tex

def main(): 
    print(tex.generate_latex_document(
        "\n".join([
            tex.generate_latex_table([
                [1, 2, 3],
                ["a", "b", "c"],
                [4, 5, 6],
            ]),
            tex.generate_latex_image("task2/artifacts/extra/image.png")
        ]))
    )
                                
if __name__ == "__main__":
    main()
