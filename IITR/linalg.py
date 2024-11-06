import numpy as np  

matrix1 = np.array([[1, 2, 5],
                   [3, 9, 1],
                   [4, 1, 1]])
matrix2 = np.array([[1, 2, -1],
                    [0, 1, 9],
                    [-1, 0, 1]])
inv1 = np.linalg.inv(matrix1)
inv2 = np.linalg.inv(matrix2)
inv3 = np.matmul(inv1, inv2)
inv3 = np.linalg.matrix_power(inv3, 2)
mat3 = np.matmul(matrix2, matrix1)
mat3 = np.linalg.matrix_power(mat3, -1)
print(np.matmul(inv3, mat3))



# print(np.dot(matrix1, matrix2))
# print(np.dot(inv1, matrix1))
# print(np.matmul(matrix1, matrix2))
# print(np.matmul(matrix1, inv1))