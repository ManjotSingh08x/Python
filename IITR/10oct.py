from math import log2
import matplotlib.pyplot as plt
# integer = int(input("Enter the number: "))

# mindivisor = integer

# for i in range(2, int(sqrt(integer)) + 1):
#     if(integer % i == 0):
#         mindivisor = i
#         break
        
# print("Min divisor is: ", mindivisor)

#hcf of 2 numbers

# def hcf(a, b): return hcf(b , a % b) if a % b else b


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Their HCF is: ", hcf(a, b))

# find x ^ y

# x = int(input("Enter base: "))
# y = int(input("Enter exponent: "))

# z = 1
# for i in range(y):
#     z *= x

# print(z)
size = 100000
x = 1
c = 0
counterList = [0 for i in range(0, size)]
def power(x, y, counterList, i):
    counterList[i] += 1
    if(y==1):
        return x
    if(y == 0):
        return 1
    if(y % 2 == 0):
        answer = power(x, y/ 2, counterList, i)
        return answer * answer
    else:
        answer1 = power(x, y % 2, counterList, i)
        answer2 = power(x, y // 2, counterList, i)
        return answer1*answer2*answer2
    
log_values = [2 * int(log2(i)) for i in range(1, size)]
log_values2 = [int(log2(i)) for i in range(1, size)]
for i in range(1, size):
    power(x, i, counterList, i)

#print(counterList)

plt.figure(1)
plt.plot(counterList)
plt.plot(log_values)
plt.plot(log_values2)
plt.show()
# x = int(input("Enter base: "))
# y = int(input("Enter exponent: "))
# print(power(x, y))
# print(c)
# print(log2(y))
#32765
#32766

