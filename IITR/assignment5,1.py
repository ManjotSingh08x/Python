# Question 1

import numpy as np

# the augmented matrix [A|B]
system = np.array([[8, 6, 2, 3, 20],
                   [3, 8, 4, 3, 24],
                   [5, 2, 6, 8, 12],
                   [9, 2, 3, 4, 14]]).astype(float)
length = len(system)  # Length is number of rows

# function to perform row operations to eliminate variables
def row_operation(row1, row2, index):
    # If the leading element in row2 is non-zero, perform the elimination
    if row2[index] != 0:
        scale_factor = -row2[index] / row1[index]
        # Update row2 to eliminate the variable in the current column (index)
        row2 += row1 * scale_factor

# function to scale a row so that the pivot element becomes 1
def scale_down(row, value):
    for i in range(len(row)):
        row[i] /= value

# convert the matrix to an upper triangular form
for i in range(0, length):
    # make the leading element = 1
    scale_down(system[i], system[i, i])
    # Perform row operations to make elements below the pivot in this column zero
    for j in range(length - 1, i, -1):
        row_operation(system[i], system[j], i)

# Display the resulting upper triangular matrix
print(system)

# Initialize a solution array
solution = np.zeros((length + 1, ))
# Perform back-substitution to solve for the variables
for i in range(length - 1, -1, -1):
    # Calculate the solution for the current variable by subtracting known values
    solution[i] = system[i, 4] - np.dot(solution + [0], system[i])

# Remove the extra element from the solution array
# i had to add an extra zero to fit into the dot product
solution = solution[:-1]
print(solution)
