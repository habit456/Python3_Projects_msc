# my goal is to create a matrix that randomly generates 1s and 0s
# for each value. And then to find the longest connection in that matrix
import numpy as np


class Matrix:
    def __init__(self, rows, columns):
        self.matrix = np.array([[0 for column in range(columns)] for row in range(rows)])
        self.rows = rows
        self.columns = columns
        self.shape = (rows, columns)

    def display(self):
        for row in self.matrix:
            print(row)

    def randomize(self):
        for r in self.matrix:
            for i, n in enumerate(r):
                r[i] += np.random.randint(0, 2)

    def flattened(self):
        flat_mat = []
        for r in self.matrix:
            flat_mat.extend(r)
        return flat_mat


"""def find_path(matrix, row_num, col_num, memory=[]):
    paths = memory.copy()
    if col_num + 1 < matrix.columns:
        if matrix[row_num][col_num + 1] == 1:
            count = 0
            for i in paths:
                if path[0]"""


np.random.seed(456)
my_matrix = Matrix(20, 10)
my_matrix.randomize()
# find_path(my_matrix, 0, 0)
print(dir(my_matrix))

