import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random x values between 0 and 50
x = np.random.rand(100) * 100
m = 2.5  # Slope
c = 5  # Intercept
noise = np.random.randn(100) * 50 # Random noise

# Calculate y based on the linear equation plus noise
# to simulate real life data
y = m * x + c + noise


# calculating derivative of error with respect to m and c,
# we arrive at two linear equations of the form
# a1 * m + b1 * c = d1
# a2 * m + b2 * c = d2

# values of all coefficients
a1 = sum([i*i for i in x])
b1 = sum(x)
d1 = sum([x[i]*y[i] for i in range(len(x))])
a2 = b1
b2 = len(x)
d2 = sum(y)

# using crammer's rule to solve for m and c
m = (d1 * b2 - d2 * b1)/(a1 * b2 - a2 * b1)
c = (d1 * a2 - d2 * a1)/(b1 * a2 - a1 * b2)

# example answer
plt.figure(1)
plt.scatter(x, y,)
x0 = [0, 100]
y0 = [c, c + 100*m]
plt.plot(x0, y0, label = 'Line', color = 'red')
plt.show()