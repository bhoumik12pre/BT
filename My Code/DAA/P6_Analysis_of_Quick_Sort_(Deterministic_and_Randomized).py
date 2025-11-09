# Program: Analysis of Quick Sort (Deterministic and Randomized)
# Aim: To implement and analyze the performance of Quick Sort using
# deterministic and randomized pivot selection strategies.

# --- Logic Behind the Problem ---
# Quick Sort is a divide-and-conquer sorting algorithm.
# It works by selecting a pivot, partitioning the array into two subarrays:
# - Left part → elements smaller than pivot
# - Right part → elements greater than pivot
# Then, it recursively sorts both parts.
#
# Deterministic Quick Sort → Pivot chosen in a fixed way (e.g., last element)
# Randomized Quick Sort → Pivot chosen randomly to avoid worst-case on sorted data.

import random
import time

# --- Deterministic Partition Function ---
def partition_deterministic(arr, low, high):
    pivot = arr[high]                     # Choose last element as pivot
    i = low - 1                           # Pointer for smaller elements

    for j in range(low, high):            # Traverse through all elements
        if arr[j] <= pivot:               # If current element smaller than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap to left part

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1                          # Return pivot index


# --- Deterministic Quick Sort Function ---
def quicksort_deterministic(arr, low, high):
    if low < high:
        pi = partition_deterministic(arr, low, high)   # Partition the array
        quicksort_deterministic(arr, low, pi - 1)      # Sort left subarray
        quicksort_deterministic(arr, pi + 1, high)     # Sort right subarray


# --- Randomized Partition Function ---
def partition_randomized(arr, low, high):
    # Logic: Randomly choose a pivot to minimize chance of worst-case performance
    rand_pivot = random.randint(low, high)   # Random index between low and high
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]  # Swap random pivot to end
    return partition_deterministic(arr, low, high)     # Partition using same logic


# --- Randomized Quick Sort Function ---
def quicksort_randomized(arr, low, high):
    if low < high:
        pi = partition_randomized(arr, low, high)      # Use random pivot each time
        quicksort_randomized(arr, low, pi - 1)         # Sort left part
        quicksort_randomized(arr, pi + 1, high)        # Sort right part


# --- Main Program ---
n = int(input("Enter number of elements: "))           # Input array size
arr = []                                               # Empty list to store elements

# Step 1: Input array elements
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Create copies for both variants
arr_deterministic = arr.copy()
arr_randomized = arr.copy()

# Step 2: Apply Deterministic Quick Sort
start_det = time.time()                                # Start timer
quicksort_deterministic(arr_deterministic, 0, n - 1)
end_det = time.time()                                  # End timer

# Step 3: Apply Randomized Quick Sort
start_rand = time.time()                               # Start timer
quicksort_randomized(arr_randomized, 0, n - 1)
end_rand = time.time()                                 # End timer

# Step 4: Display results
print("\n--- Sorted Arrays ---")
print("Deterministic Quick Sort Result:", arr_deterministic)
print("Randomized Quick Sort Result:", arr_randomized)

# Step 5: Time analysis
print("\n--- Time Analysis ---")
print(f"Deterministic Quick Sort Time: {(end_det - start_det) * 1_000_000:.2f} microseconds")
print(f"Randomized Quick Sort Time: {(end_rand - start_rand) * 1_000_000:.2f} microseconds")

# --- Time and Space Complexity Analysis ---
print("\n--- Complexity Analysis ---")
print("Deterministic Quick Sort:")
print("   Best Case Time Complexity: O(n log n)")
print("   Average Case Time Complexity: O(n log n)")
print("   Worst Case Time Complexity: O(n²) (when pivot always picks smallest/largest element)")
print("   Space Complexity: O(log n) due to recursion stack")

print("\nRandomized Quick Sort:")
print("   Best Case Time Complexity: O(n log n)")
print("   Average Case Time Complexity: O(n log n)")
print("   Worst Case Time Complexity: O(n²) (very rare due to random pivot)")
print("   Space Complexity: O(log n)")





# Enter number of elements: 6
# Enter element 1: 45
# Enter element 2: 12
# Enter element 3: 7
# Enter element 4: 89
# Enter element 5: 32
# Enter element 6: 50

# --- Sorted Arrays ---
# Deterministic Quick Sort Result: [7, 12, 32, 45, 50, 89]
# Randomized Quick Sort Result: [7, 12, 32, 45, 50, 89]

# --- Time Analysis ---
# Deterministic Quick Sort Time: 135.42 microseconds
# Randomized Quick Sort Time: 118.77 microseconds

# --- Complexity Analysis ---
# Deterministic Quick Sort:
#    Best Case Time Complexity: O(n log n)
#    Average Case Time Complexity: O(n log n)
#    Worst Case Time Complexity: O(n²)
#    Space Complexity: O(log n)

# Randomized Quick Sort:
#    Best Case Time Complexity: O(n log n)
#    Average Case Time Complexity: O(n log n)
#    Worst Case Time Complexity: O(n²)
#    Space Complexity: O(log n)
