a = [1, 3, 5, 0, 2, 7, 9]

def partition(A: list[int] , start, end):
    pivot = A[end]
    i = start-1
    for j in range(start, end):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[j], A[i+1] = A[i+1], A[j]
    return i+1

print(a)
print(partition(a, 0, len(a)-1))
print(a)
