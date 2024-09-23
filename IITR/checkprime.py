from math import sqrt

def checkprime(number):
    if number == 1:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number%i == 0:
            return False
    return True

number = int(input("Enter the number: "))
print(checkprime(number))
    