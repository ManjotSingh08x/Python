arr = [9, 4, 3, 8, 10, 2, 5]

def max_heapify(arr, n, i):
    l = i * 2 + 1
    r = i * 2 + 2
    largest = i
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heapsort(arr, n):
    for i in range(n-1, -1, -1):
        max_heapify(arr, n, i)
    print(arr)
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)
        print(arr)

heapsort(arr, len(arr))