# Program: Recursive and Non-Recursive Fibonacci
# Aim: To calculate Fibonacci numbers using both methods
# and analyze their time and space complexity.
#Recursive = uses function calls to repeat.

#Non-Recursive = uses loops to repeat.

# --- Non-Recursive (Iterative) Fibonacci ---
def fib_iterative(n):              # Define a function to find the nth Fibonacci number using iteration (loop method)

    if n <= 1:                     # Base condition: if n is 0 or 1,
        return n                   # then the Fibonacci number is the same as n itself (F(0)=0, F(1)=1)

    # Logic: Fibonacci series starts with 0 and 1.
    # Example: 0, 1, 1, 2, 3, 5, 8 ...
    # So we assign a = 0 (first term), b = 1 (second term)
    a, b = 0, 1                    # Initialize first two Fibonacci numbers

    # Logic: We already know first two numbers, so loop starts from index 2 (third number)
    for i in range(2, n + 1):      # Repeat from 2 to n to calculate further terms
        c = a + b                  # Next Fibonacci number is the sum of previous two (Fn = Fn-1 + Fn-2)
        a = b                      # Shift 'b' to 'a' → move one step ahead in the series
        b = c                      # Shift 'c' to 'b' → update current Fibonacci value

    # After the loop ends, 'b' holds the last calculated Fibonacci number (i.e., F(n))
    return b                       # Return nth Fibonacci number


# --- Recursive Fibonacci ---
def fib_recursive(n):              # Define a function to find the nth Fibonacci number using recursion

    # Logic: Fibonacci follows the formula F(n) = F(n-1) + F(n-2)
    # but for first two terms, F(0)=0 and F(1)=1 (base conditions)
    if n <= 1:                     # Base condition to stop recursion
        return n                   # Directly return n if it is 0 or 1

    # Logic: For any other n, call the same function for previous two terms
    # and add their results to get current Fibonacci number
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)   # Recursive relation


# --- Main Program ---
n = int(input("Enter number of terms: "))     # Take user input for number of Fibonacci terms to print

print("\nFibonacci Series using Iteration:")  # Display title for iterative Fibonacci
for i in range(n):                            # Loop through 0 to n-1
    print(fib_iterative(i), end=" ")          # Print each Fibonacci number using iterative method

print("\n\nFibonacci Series using Recursion:") # Display title for recursive Fibonacci
for i in range(n):                             # Loop through 0 to n-1
    print(fib_recursive(i), end=" ")           # Print each Fibonacci number using recursion


# --- Time and Space Complexity Analysis ---
print("\n\n--- Time and Space Complexity ---")
print("Iterative Method:")
print("   Time Complexity: O(n)")             # Takes linear time due to single loop
print("   Space Complexity: O(1)")            # Constant space as only 3 variables used (a, b, c)

print("\nRecursive Method:")
print("   Time Complexity: O(2^n)")           # Exponential time due to repeated recursive calls
print("   Space Complexity: O(n)")            # Linear space due to recursion stack





# Enter number of terms: 7

# Fibonacci Series using Iteration:
# 0 1 1 2 3 5 8 

# Fibonacci Series using Recursion:
# 0 1 1 2 3 5 8 

# --- Time and Space Complexity ---
# Iterative Method:
#    Time Complexity: O(n)
#    Space Complexity: O(1)

# Recursive Method:
#    Time Complexity: O(2^n)
#    Space Complexity: O(n)
