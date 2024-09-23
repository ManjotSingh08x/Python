A = [2, 4, 1, 0, 9]

def bubblesort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    
    return A

def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j+1] = key
    return A

print(insertionsort(A))