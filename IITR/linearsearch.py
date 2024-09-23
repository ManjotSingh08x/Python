#print(2*3.14*(int(float(input()))))

def search(A: list[int], x: int):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

def delete(A: list[int], x: int):
    # index = search(A, x)
    # for i in range(index, len(A)-1):
    #     A[i] = A[i+1]
    # A.pop(len(A)-1)
    # return A
    A.pop(search(A,x))
    return A

if __name__ == "__main__":
    A = [1,2,3,4,5, 99]
    print(search(A, 4))
    A