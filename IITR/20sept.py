def sortList(list):
    M = []
    while list:
        if len(M) == 0:
            M.append(list.pop())
        element = list.pop()
        for i in range(len(M)):
            if element <= M[i]:
                M.insert(i, element)
                print(M)
                break
            elif i == len(M) - 1:
                M.append(element)
    return M

a = [1,1, 5, 7, 3, 1, 9]
print(sortList(a))

def countVowel(string):
    count = 0
    for ch in string.lower():
        if ch in 'aeiou':
            count += 1
            
    return count

print(countVowel("Aneumonoultramicroscopicsilicovolcanoconiosis"))