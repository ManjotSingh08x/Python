x = float(input("Enter a number (greater than 1): "))
y = 1
eps = 0.0001
while (x/y >= y + eps) or (x/y <= y - eps): 
    y = (x/y + y)/2
print(y)