import matplotlib.pyplot as plt
import math
#import numpy as np

plt.figure(1)
valuepi = math.pi
t = [-valuepi*2 + i *0.01 for i in range(0, int(400 * valuepi))]
s = []
for i in t:
    s.append(math.sin(i))
plt.plot(t,s)
plt.show()
print(math.pi)