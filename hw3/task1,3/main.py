import numpy as np
import matrix as mt

def main():
    np.random.seed(0)

    matrixA = mt.Matrix([[-10, 110]])
    matrixB = mt.Matrix([[2], [1]])

    matrixC = mt.Matrix([[10, 20], [30, 40]])
    matrixD = mt.Matrix([[2], [1]])

    assert hash(matrixA) == hash(matrixC)

    matrixAB = matrixA @ matrixB
    matrixCD = matrixC @ matrixD

    # print(matrixA)
    # print(matrixB)
    # print(matrixC)
    # print(matrixD)

    # print(matrixAB)
    # print(matrixCD)

    # print("hash AB matrix:", hash(matrixAB))
    # print("hash CD matrix:", hash(matrixCD))


if __name__ == "__main__":
    main()

