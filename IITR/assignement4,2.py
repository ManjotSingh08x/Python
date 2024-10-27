import time
import matplotlib.pyplot as plt

# fibonnaci using recursion
def fibRC(n, r):
    # Increment the recursive call counter
    r[0] += 1
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibRC(n-1, r) + fibRC(n-2, r)

# Fibonacci using dynamic programming (DP)
def fibDP(n, r, d={1: 0, 2: 1}):
    # Increment the recursive call counter
    r[0] += 1

    if n in d:
        return d[n]

    else:
        d[n] = fibDP(n-1, r, d) + fibDP(n-2, r, d)
        return d[n]


x_values = [i for i in range(1, 33)]
recursive_time = []  # To store time taken by the recursive function
dp_time = []  # To store time taken by the DP function

# Function to calculate time taken by both recursive and DP methods
def calculate_time(n):
    r = [0]  # Initialize recursive call counter
    
    # Measure time for recursive Fibonacci
    start1 = time.time()
    fibRC(n, r)
    end1 = time.time()
    recursive_time.append(end1 - start1)  # Store the time taken
    print(end1-start1)
    # Measure time for DP Fibonacci
    r = [0]  # Reset recursive call counter
    start2 = time.time()
    fibDP(n, r)
    end2 = time.time()
    dp_time.append(end2 - start2) 
    print( end2 - start2) # Store the time taken

# Calculate time for each Fibonacci number in x_values
for x_value in x_values:
    calculate_time(x_value)

# Plotting the time results
plt.figure(1)
plt.plot(x_values, recursive_time, label='Recursive', scaley=1)
plt.plot(x_values, dp_time, label='DP')
plt.yscale('log')  # Set y-axis to logarithmic scale to show the difference clearly
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.title('Time Comparison: Recursive vs DP')


recursive_calls = []  # To store number of recursive calls for the recursion
dp_calls = []  # To store number of recursive calls for DP

# Function to calculate the number of recursive calls
def calculate_calls(n):
    recursive_call = [0]  
    fibRC(n, recursive_call)  # Call recursive Fibonacci
    recursive_calls.append(recursive_call[0])  # Store the number of recursive calls
    
    dp_call = [0]  # Initialize counter for DP recursive calls
    dic = {1: 0, 2: 1}  # Reset the dictionary for DP
    fibDP(n, dp_call, dic)  # Call DP Fibonacci
    dp_calls.append(dp_call[0])  # Store the number of DP recursive calls

# Calculate the number of calls for each Fibonacci number in x_values
for x_value in x_values:
    calculate_calls(x_value)

# Plotting the number of recursive calls
plt.figure(2)
plt.plot(x_values, recursive_calls, label='Recursive Calls')
plt.plot(x_values, dp_calls, label='DP Calls')
plt.yscale('log')  # Set y-axis to logarithmic scale
plt.xlabel('n')
plt.ylabel('Number of Calls')
plt.legend()
plt.title('Number of Calls: Recursive vs DP')
plt.show()
