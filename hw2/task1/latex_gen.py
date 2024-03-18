import typing as tp

def generate_latex_table(data: tp.List[tp.List[str]]):
    num_cols = max(len(row) for row in data)

    latex_code = "\\documentclass{article}\n"
    latex_code += "\\begin{document}\n"
    latex_code += "\\begin{tabular}{|" + "|".join(["c"] * num_cols) + "|}\n"

    for row in data:
        latex_code += " & ".join(str(cell) for cell in row)
        latex_code += " \\\\\n"

    latex_code += "\\end{tabular}\n"
    latex_code += "\\end{document}\n"

    return latex_code
