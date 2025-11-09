# Program: 0/1 Knapsack Problem using Dynamic Programming
# Aim: To solve the 0/1 Knapsack problem using the Dynamic Programming approach
# where each item can either be taken completely or not at all (no fractions allowed).

# --- Logic Behind the Problem ---
# In the 0/1 Knapsack problem, we have a set of items, each with a value and a weight.
# We must select items to maximize total value without exceeding the knapsack capacity.
# Unlike fractional knapsack, we cannot take partial items — only 0 (not taken) or 1 (taken).
# The Dynamic Programming approach builds a table that stores the best possible result
# for every subproblem (smaller capacities and item subsets).

# --- Function to solve 0/1 Knapsack using Dynamic Programming ---
def knapsack_01(values, weights, capacity):
    n = len(values)                               # Total number of items

    # Step 1: Create a 2D DP table with (n+1) rows and (capacity+1) columns
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    # Step 2: Build table dp[][] bottom-up
    for i in range(1, n + 1):                     # Loop through items
        for w in range(1, capacity + 1):          # Loop through all capacities
            if weights[i - 1] <= w:               # If current item can fit in capacity w
                # Logic: choose maximum of including item or excluding item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # include item
                    dp[i - 1][w]                                    # exclude item
                )
            else:
                # If item can't fit, we just carry over previous best
                dp[i][w] = dp[i - 1][w]

    # Step 3: The last cell dp[n][capacity] contains the maximum achievable value
    return dp[n][capacity]


# --- Main Program ---
n = int(input("Enter number of items: "))          # Number of available items
values = []                                        # List to store item values (profits)
weights = []                                       # List to store item weights

# Step 1: Input value and weight for each item
for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

# Step 2: Input total knapsack capacity
capacity = int(input("Enter capacity of knapsack: "))

# Step 3: Call knapsack function to compute result
max_value = knapsack_01(values, weights, capacity)

# Step 4: Display the final result
print(f"\nMaximum value that can be placed in the knapsack = {max_value}")

# --- Time and Space Complexity Analysis ---
print("\n--- Time and Space Complexity ---")
print("Time Complexity: O(n * W)  (where n = number of items, W = knapsack capacity)")
print("Space Complexity: O(n * W)  (for storing DP table)")





# Enter number of items: 3
# Enter value of item 1: 60
# Enter weight of item 1: 10
# Enter value of item 2: 100
# Enter weight of item 2: 20
# Enter value of item 3: 120
# Enter weight of item 3: 30
# Enter capacity of knapsack: 50

# Maximum value that can be placed in the knapsack = 220

# --- Time and Space Complexity ---
# Time Complexity: O(n * W)
# Space Complexity: O(n * W)
