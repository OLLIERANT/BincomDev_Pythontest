#!/usr/bin/python3
"""
Script that generates random 4 digits number of 0s and 1s,
and convert the generated number to base 10.
"""

import sys
import random


# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert the binary number to decimal
decimal_number = int(binary_number, 2)

print(f"Generated Binary Number: {binary_number}")
print(f"Decimal Equivalent: {decimal_number}")
