#!/usr/bin/python3
"""
Script that prints the variance of the colors 
worn throughout the week
"""

import sys
from collections import Counter

# Execute code when it runs as a script
if __name__ == "__main__":

    # Colors data for each day of the week
    colors_per_day = [
        ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
        ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
        ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
    ]

    # Define numerical values for each color (you can customize this list)
    color_values = {
        "GREEN": 1,
        "YELLOW": 2,
        "BROWN": 3,
        "BLUE": 4,
        "PINK": 5,
        "BLEW": 6,
        "RED": 7,
        "WHITE": 8,
        "ORANGE": 9,
        "CREAM": 10,
        "BLACK": 11,
    }

    # Correct the typo in the colors_per_day list ("BLEW" should be "BLUE")
    for day in colors_per_day:
        for i in range(len(day)):
            if day[i] == "BLEW":
                day[i] = "BLUE"

	# Flatten the list of colors for the week and convert to numerical values
    all_colors = [color_values.get(color, 0) for day in colors_per_day for color in day]

    # Calculate the mean color
    total_colors = len(all_colors)
    mean_color = sum(all_colors) / total_colors

    # Calculate the variance
    variance = sum((color - mean_color) ** 2 for color in all_colors) / total_colors

    print(f"The variance of the colors is: {variance}")
