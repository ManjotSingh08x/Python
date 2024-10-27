import time
import matplotlib.pyplot as plt

# Fibonnaci using DP
def calculate_fibDP(n):

    recursive_counter = [0]     # Counts the number of times the function is called
    lookup_counter = [0]        # Counts the number of successful lookups in the DP dictionary
    dictionary_counter = [0]    # Counts the number of times the DP dictionary is updated

    dp = {1: 0, 2: 1}           
    start = time.time()          # Start the timer

    # Call the Fibonacci DP function
    fibDP(n, recursive_counter, lookup_counter, dictionary_counter, dp)

    end = time.time()            # End the timer
    time_taken = end - start     # Calculate the time taken for the calculation


    result = [
        recursive_counter[0],    # Number of recursive calls
        lookup_counter[0],       # Number of lookups performed
        dictionary_counter[0],   # Number of times the dictionary is updated
        time_taken               # Time taken to compute the Fibonacci number
    ]
    return result

# Recursive Fibonacci function with counters for DP
def fibDP(n, r, l, d, dp):
    r[0] += 1  # Increment recursive call counter
    if n in dp: 
        l[0] += 1  # Increment lookup counter
        return dp[n]
    else:
        d[0] += 1  # Increment dictionary update counter

        dp[n] = fibDP(n - 1, r, l, d, dp) + fibDP(n - 2, r, l, d, dp)
        return dp[n]

# Function to display the results
def display_result(result_list, n):
    print(f"For value n = {n}:")
    print(f"No. of recursive calls: {result_list[0]}")
    print(f"No. of successful lookups: {result_list[1]}")
    print(f"No. of dictionary updates: {result_list[2]}")
    print(f"Time taken to compute: {result_list[3]:.6f} seconds")

# Main execution
n = int(input("Enter a number: "))
display_result(calculate_fibDP(n), n)

