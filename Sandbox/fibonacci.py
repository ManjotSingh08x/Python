# def abs1(x):
#     return -x if x < 0 else x

# print(abs1(-100), abs1(33), abs1(0.0))
import time
import sys
sys.set_int_max_str_digits(45000)

# def fib(n):
#     fib1 = 1
#     fib2 = 1
#     fib3 = 1
#     for i in range(2, n+1):
#         fib3 = fib1 + fib2
#         fib1 = fib2
#         fib2 = fib3
#     return fib3
count = 0
def fib(n):
    global count
    count += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
# begin = time.time()
# print(fib(35))
# endtime = time.time()
# print(endtime-begin)

#print(fib(int(input("Enter number: "))))