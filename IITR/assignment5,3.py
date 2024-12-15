import matplotlib.pyplot as plt
import numpy as np

number = int(input("Enter number of data points: "))
y = []
for i in range(number):
    value = int(input("Enter value: "))
    y.append(value)

x = [i for i in range(1, number + 1)]

# values of all coefficients
squared = sum([i*i for i in x])
sumofx = sum(x)
xintoy = sum([x[i]*y[i] for i in range(len(x))])
n = len(x)
sumofy = sum(y)

# using crammer's rule to solve for m and c
m = (xintoy * n - sumofy * sumofx)/(squared * n - sumofx * sumofx)
c = (xintoy * sumofx - sumofy * squared)/(sumofx * sumofx - squared * n)

print(m, c)