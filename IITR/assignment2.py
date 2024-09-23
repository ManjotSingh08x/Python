#Question 1
import random 

# Generate a list of 25 random integers between 0 and 25
a = [random.randint(0, 25) for i in range(25)]

def merge(list1, list2):
    i, j = 0, 0
    arr = []  # Array to hold the merged result

    # Merge elements from both lists
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            arr.append(list2[j])  # Append from list2 if smaller
            j += 1
        else:
            arr.append(list1[i])  # Append from list1 if smaller
            i += 1

    # Add remaining elements from either list
    arr.extend(list1[i:] or list2[j:])
    return arr

def mergesort(a):
    # Base case: if the list is of length 1, return it
    if len(a) == 1:
        return a
    
    # Split the list into two halves
    middle = len(a) // 2
    left = mergesort(a[:middle])   # Recursively sort the left half
    right = mergesort(a[middle:])  # Recursively sort the right half

    return merge(left, right)  # Merge the sorted halves


print(mergesort(a))

# Question 2
b = [random.randint(0,99) for i in range(200)]

# this function takes as input the data list which contains multiple repetitions
# of various elements. the frequency of each class interval is stored in the 
# corresponding index inside the histogram list
# eg if data = [2, 2, 45, 56] then historgram will become 
# histogram = [2, 0, 0, 0, 1, 1]
def createHistogram(data):
    histogram = [0]*10
    for i in data:
        histogram[i%10] += 1
        
    return histogram

#displays the histogram in a formatted manner
def printHistogram(hist):

    print("  ", end='')
    for i in range(len(hist)):
        asterisks = '*'*hist[i]
        print(i*10, '-' , i*10+9, ":", asterisks )
        
printHistogram(createHistogram(b))

# Question 3

# this function returns the result of f(x) = x^4 - 4
def poly(x):
    return x**4 - 4

# the derivate of f(x) is f'(x) = 4x^3
def deriv(x):
    return 4*x**3

# the newton raphson method states that for closer and closer approximations of roots 
# of a function, we can iterate x_n = x_n-1 - f(x)/f'(x)
# so x_n approaches root of f(x)
def newton(initial):
    x = initial
    eps = 1e-10
    while poly(x) > eps or poly(x) < - eps:
        x -= poly(x)/deriv(x)
    
    return x

#we can start from any value as long as its not near any extremum
#print("Root of function is:", newton(10))

#Question 4


def decimaltobinary(n):
    binary = ''
    # special case for n = 0
    
    if n == 0:
        return '0'
    while n > 0:
        # Prepend the remainder of n divided by 2 (0 or 1) to the binary string
        # This constructs the binary representation in reverse order
        binary = str(n % 2) + binary
        n = n // 2
    return binary 

# print(decimaltobinary(128)) # expect 10000000
# print(decimaltobinary(127)) # expect 1111111
# print(decimaltobinary(10))  # expect 1010
# print(decimaltobinary(49))  # expect 110001

# Question 5

def isprime(n, primelist):
    # Consider 1 and negative numbers to be non-prime
    if n <= 1:
        return False
    
    # Calculate the square root of n for limiting the checks
    sqrt_n = n**0.5
    
    # Iterate over the list of known primes
    for prime in primelist:
        # If n is divisible by any prime, it is composite
        if n % prime == 0:
            return False
        
        # If the prime is greater than the square root of n,
        # no further checks are necessary
        if prime > sqrt_n:
            # Add n to the prime list as it's determined to be prime
            primelist.append(n)
            break
    
    # If no divisors were found, n is prime
    return True

def primefactors(n):
    # Initialize an empty list to store the prime factors
    factors = []
    # Initialize an empty list to store known primes
    primelist = []
    
    # Iterate from 0 to n to find prime numbers
    for i in range(n + 1):
        # Check if i is a prime number using the isprime function
        if isprime(i, primelist):
            # While n is divisible by the prime number i
            while n % i == 0:
                # Divide n by i and append i to the factors list
                n = n // i
                factors.append(i)
    
    # Sort the factors list to ensure factors are in ascending order
    factors.sort()
    
    # Return the list of prime factors
    return factors


# print("prime factors of", 10, "are: ", primefactors(10))
# print("prime factors of", 64, "are: ", primefactors(64))
# print("prime factors of", 360, "are: ", primefactors(360))

# Question 6
def binarysearch(list, x, begin, end):
    # Check if the search space is valid
    if begin >= end:
        # If the current position matches x, return the index
        if list[begin] == x:
            return begin
        else:
            # x is not found, return -1
            return -1 
    else:
        # Calculate the middle index of the current search space
        mid = (begin + end) // 2
        
        # If the middle element is x, return the index
        if list[mid] == x:
            return mid
        # If the middle element is less than x, search in the right half
        elif list[mid] < x:
            return binarysearch(list, x, mid + 1, end)
        # If the middle element is greater than x, search in the left half
        else:
            return binarysearch(list, x, begin, mid - 1)

# create a list of random numbers. and sort them to apply binary search
# sorting is done through merge sort that has been implemented previously
c = mergesort(random.sample(range(50), 25))
#print(c)
# print the position of 23 in the sorted list
# it is assumed that each element occurs once
# if not, binary search may give some other index that is not the first one
#print(binarysearch(c, 23, 0, len(c)))
#verify that the same index is returned by the index function
#print(c.index(23))
        
            
    
    