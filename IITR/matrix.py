rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): 
            print(matrix[i][j], end=' ')
        print()

matrix = []
for i in range(rows):
    a = []
    for j in range(columns): 
        a.append(int(input(f'Enter value of index {i+1},{j+1}: ')))
    matrix.append(a)

print("Your matrix is: ")
printMatrix(matrix)

transpose = []
for i in range(columns):
    b = []
    for j in range(rows):
        b.append(matrix[j][i])
    transpose.append(b)

print("Its transpose is: ")
printMatrix(transpose)