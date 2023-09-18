#!/usr/bin/python3
"""
Write a program to sum the first 50 fibonacci sequence.
"""

import sys

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Calculate the first 50 Fibonacci numbers
n = 50
fib_sequence = fibonacci(n)

# Sum the first 50 Fibonacci numbers
fib_sum = sum(fib_sequence)

print(f"The sum of the first {n} Fibonacci numbers is: {fib_sum}")

# Execute code when it runs as a script
if __name__ == '__main__':
    fibonacci(n)
