import numpy as np
import matrix_mixin as mt

def main():
    np.random.seed(0)

    np_matrix1 = np.random.randint(0, 10, (10, 10))
    np_matrix2 = np.random.randint(0, 10, (10, 10))

    matrix1 = mt.Matrix(np_matrix1)
    matrix2 = mt.Matrix(np_matrix2)


    # print(matrix1 + matrix2)
    # print(matrix1 * matrix2)
    # print(matrix1 @ matrix2)


if __name__ == "__main__":
    main()

