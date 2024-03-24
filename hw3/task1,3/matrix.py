class HashMixin():
    # hash is calculated as sum of all elements of the iterable object
    def __hash__(self) -> int:
        return int(sum(self))

class Matrix(HashMixin):
    def __init__(self, rows):
        self.rows = rows
        self.shape = (len(rows), len(rows[0]))

    def __str__(self):
        result = "["
        for row in self.rows:
            result += "[" + " ".join(map(str, row)) + "]\n"
        return result.rstrip() + "]"

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices dimensions incompatible for element-wise multiplication")

        result = [[self.rows[i][j] * other.rows[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(result)

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices dimensions incompatible for `add` operation")

        result = [[self.rows[i][j] + other.rows[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        return Matrix(result)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Matrices dimensions incompatible for multiplication")

        result = [[0 for _ in range(other.shape[1])] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(self.shape[1]):
                    result[i][j] += self.rows[i][k] * other.rows[k][j]

        return Matrix(result)
    
    def __iter__(self):
        # Iterate over the elements of the matrix
        for row in self.rows:
            for element in row:
                yield element
    
