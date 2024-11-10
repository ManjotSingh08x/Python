import numpy as np  

matrix1 = np.array([[1, 2, 5],
                   [3, 9, 1],
                   [4, 1, 1]])
matrix2 = np.array([[1, 2, -1],
                    [0, 1, 9],
                    [-1, 0, 1]])

print(np.linalg.matrix_power(matrix1, 0))
inv1 = np.linalg.inv(matrix1)
inv2 = np.linalg.inv(matrix2)
inv3 = np.matmul(inv1, inv2)
inv3 = np.linalg.matrix_power(inv3, 2)
mat3 = np.matmul(matrix2, matrix1)
mat3 = np.linalg.matrix_power(mat3, -1)
print(np.matmul(inv3, mat3))
print(matrix1, '\n', matrix1.T)

rows = int(input("enter number of rows: "))
column = int(input('enter number of columns'))

enter  = np.zeros((rows, column))

for i in range(len(enter)):
    for j in range(len(enter[i])):
        enter[i, j] = float(input(f"enter {i},{j}: "))

print(enter)




# print(np.dot(matrix1, matrix2))
# print(np.dot(inv1, matrix1))
# print(np.matmul(matrix1, matrix2))
# print(np.matmul(matrix1, inv1))