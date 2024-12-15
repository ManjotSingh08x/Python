import numpy as np

matrix = np.array([[8, 6, 2, 3, 20],
                   [3, 8, 4, 3, 24],
                   [5, 2, 6, 8, 12],
                   [9, 2, 3, 4, 14]]).astype(float)
num_rows = len(matrix)

def operation(a_row, b_row, column_idx):
    scalar = b_row[column_idx] / a_row[column_idx]
    temp_row = np.copy(a_row)
    temp_row *= scalar
    b_row -= temp_row

def divide_row(row, divisor):
    result_row = np.copy(row)
    for idx in range(len(row)):
        result_row[idx] /= divisor
    return result_row

def perform_back_substitution(matrix, n_rows):
    results = np.zeros((n_rows,))
    for idx in range(n_rows - 1, -1, -1):
        temp_sum = matrix[idx, 4]
        for sub_idx in range(idx + 1, n_rows):
            temp_sum -= results[sub_idx] * matrix[idx, sub_idx]
        results[idx] = temp_sum / matrix[idx, idx]
    return results

def gauss_jordan(matrix, n_rows):
    for i in range(n_rows):
        matrix[i] = divide_row(matrix[i], matrix[i, i])

        for j in range(n_rows - 1, i, -1):
            operation(matrix[i], matrix[j], i)

    return perform_back_substitution(matrix, n_rows)

solution = gauss_jordan(matrix, num_rows)
print(solution)