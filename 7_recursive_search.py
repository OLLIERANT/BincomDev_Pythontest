#!/usr/bin/python3
"""
write a recursive searching algorithm to search for a number
entered by user in a list of numbers.
"""

import sys

# function that performs a recursive binary search in a sorted list of numbers to find a target value
def binary_search_recursive(numbers, target, left=0, right=None):
    if right is None:
        right = len(numbers) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return binary_search_recursive(numbers, target, mid + 1, right)
    else:
        return binary_search_recursive(numbers, target, left, mid - 1)

# define list to search through
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# value the user wants to find
target = 7

result = binary_search_recursive(numbers, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found")

# Execute code when it runs as a script
if __name__ == "__main__":
    binary_search_recursive(numbers, target, left=0, right=None)
