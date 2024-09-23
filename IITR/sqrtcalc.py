n = float(input("Enter an integer: "))

#using bisection search
y = 1.0 
epsilon = 0.00001 #corresponds to the presicion we require
nexty = n/y #nexty is the next iteration of y 

counter1 = 0 #we count the number of iterations using this variable
while nexty > y + epsilon or nexty < y - epsilon: # this defines a range of precision (sqrt - epsilon to sqrt + epsilon)
    nexty = n/y
    y = (nexty + y)/2
    counter1 += 1

print("Solution using bisection search: ", y)
print("Iterations required: ", counter1)

#using exhaustive enumeration
z = 0
eps1 = 0.1 # for low precision but fast enumeration

counter2 = 0
while z*z <= n:
    z += eps1
    counter2 += 1

eps2 = 0.0001 # for high precision but slower enumeration when we approach the answer
while z*z >= n: #we overshoot on the lower precision so we go back at higher precision
    z -= eps2
    counter2 += 1
    
print("Solution using exhaustive enumeration: ", z)
print("Iterations required: ", counter2)
