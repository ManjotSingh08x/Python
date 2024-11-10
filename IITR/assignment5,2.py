import numpy as np

# Define matrix A
A= np.array([[8, 6, 2, 3],
            [3, 8, 4, 3],
            [5, 2, 6, 8],
            [9, 2, 3, 4]]).astype(float)



length = len(A)
Lower = np.identity(length)  # Initialize L as an identity matrix for the lower triangular matrix
Upper = np.zeros((length, length))  # Initialize U as a zero matrix for the upper triangular matrix

# LU decomposition
for i in range(length):
    # Compute U's row (i.e., U[i][j] for all j >= i)
    for j in range(i, length):
        # Calculate U[i, j] as A[i, j] minus the dot product of the corresponding
        # elements in the lower and upper parts up to the i-th element.
        Upper[i, j] = A[i, j] - np.dot(Upper[:i, j], Lower[i, :i])
    
    # Compute L's column (i.e., L[j][i] for all j > i) since it is lower traingle
    for j in range(i + 1, length):
        # Calculate L[j, i] by dividing the result of A[j, i] minus the dot product of
        # corresponding elements in U and L up to the i-th element by U[i, i].
        Lower[j, i] = (A[j, i] - np.dot(Upper[:i, i], Lower[j, :i])) / Upper[i, i]

# Display the resulting U and L matrices
print("Upper Triangular Matrix U:")
print(Upper)
print("Lower Triangular Matrix L:")
print(Lower)

# Define the vector b (right-hand side of Ax = b)
b = np.array([20, 24, 12, 14], dtype=float)

# Step 1: Solve Lc = b using forward substitution
c = np.zeros((length,))  # Initialize c as a zero vector
for i in range(length):
    # Calculate each c[i] by subtracting the dot product of L[i, :i] and c[:i] from b[i]

    c[i] = b[i] - np.dot(Lower[i, :i], c[:i])

# Step 2: Solve Ux = c using back substitution
x = np.zeros((length,))  # Initialize x as a zero vector
for i in range(length - 1, -1, -1):
    # Calculate each x[i] by subtracting the dot product of U[i, i+1:] and x[i+1:]
    # from c[i], then divide by U[i, i]
    x[i] = (c[i] - np.dot(Upper[i, i+1:], x[i+1:])) / Upper[i, i]

# Final solution x for the system Ax = b
print("\nSolution x:")
print(x)

# Verify the solution by computing Ax and comparing it to b
print("Verification:")
print(np.dot(A, x))


