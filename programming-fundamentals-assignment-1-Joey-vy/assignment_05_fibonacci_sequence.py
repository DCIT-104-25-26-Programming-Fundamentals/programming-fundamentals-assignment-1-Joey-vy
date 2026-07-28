# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return
        
    fib_list = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_list.append(a)
        next_val = a + b
        a = b
        b = next_val
        
    print("Fibonacci sequence:", *fib_list)


def check_fibonacci(num):
    if num < 0:
        print(f"{num} is NOT a Fibonacci number.")
        return

    a, b = 0, 1
    is_fib = False
    
    while a <= num:
        if a == num:
            is_fib = True
            break
        next_val = a + b
        a = b
        b = next_val
        
    if is_fib:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")

if __name__ == "__main__":
    n_terms = int(input("How many terms? "))
    generate_fibonacci(n_terms)
    
    print() 
    check_num = int(input("Enter a number to check: "))
    check_fibonacci(check_num)
