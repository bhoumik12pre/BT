# Program: Fractional Knapsack Problem using Greedy Method
# Aim: To solve the fractional knapsack problem using a greedy strategy
# where items are selected based on maximum value-to-weight ratio.

# --- Logic Behind the Problem ---
# In a fractional knapsack, we can take fractions of items.
# The goal is to maximize total value within a given weight capacity.
# Greedy choice: pick the item with the highest value/weight ratio first.

# --- Function to solve fractional knapsack ---
def fractional_knapsack(value, weight, capacity):
    # Step 1: Calculate value-to-weight ratio for each item
    ratio = []
    for i in range(len(value)):
        ratio.append(value[i] / weight[i])        # ratio = value / weight

    # Step 2: Combine item data into tuples for easy sorting
    # Each tuple = (ratio, value, weight)
    items = list(zip(ratio, value, weight))

    # Step 3: Sort items in descending order of ratio (highest first)
    items.sort(reverse=True, key=lambda x: x[0])   # Greedy: pick best ratio first

    total_value = 0.0        # Variable to store total profit/value
    remaining_capacity = capacity   # Track how much capacity is left

    # Step 4: Pick items one by one
    for r, v, w in items:
        if remaining_capacity == 0:     # Stop when bag is full
            break

        if w <= remaining_capacity:
            # If item can fit completely, take it all
            total_value += v
            remaining_capacity -= w
            print(f"Took 100% of item (value={v}, weight={w})")
        else:
            # If item can't fit fully, take only the fraction that fits
            fraction = remaining_capacity / w
            total_value += v * fraction
            print(f"Took {fraction*100:.2f}% of item (value={v}, weight={w})")
            remaining_capacity = 0       # Bag is now full

    return total_value


# --- Main Program ---
n = int(input("Enter number of items: "))     # Number of items available

value = []       # List to store values (profit)
weight = []      # List to store weights

# Step 1: Input values and weights
for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

# Step 2: Input total capacity of knapsack
capacity = float(input("Enter capacity of knapsack: "))

# Step 3: Call the function to get maximum value
max_value = fractional_knapsack(value, weight, capacity)

# Step 4: Display final result
print(f"\nMaximum value in Knapsack = {max_value:.2f}")

# --- Time and Space Complexity Analysis ---
print("\n--- Time and Space Complexity ---")
print("Time Complexity: O(n log n)  (due to sorting of items based on ratio)")
print("Space Complexity: O(n)       (for storing value, weight, and ratio lists)")




# Enter number of items: 3
# Enter value of item 1: 60
# Enter weight of item 1: 10
# Enter value of item 2: 100
# Enter weight of item 2: 20
# Enter value of item 3: 120
# Enter weight of item 3: 30
# Enter capacity of knapsack: 50

# Took 100% of item (value=60.0, weight=10.0)
# Took 100% of item (value=100.0, weight=20.0)
# Took 66.67% of item (value=120.0, weight=30.0)

# Maximum value in Knapsack = 240.00

# --- Time and Space Complexity ---
# Time Complexity: O(n log n)
# Space Complexity: O(n)
