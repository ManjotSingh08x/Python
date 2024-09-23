import time 
import fibonacci
import bleach 

begin = time.time()
print(fibonacci.fib(35))
end = time.time()
print(end - begin)
print(fibonacci.count)