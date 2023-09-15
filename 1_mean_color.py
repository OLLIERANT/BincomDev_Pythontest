#!/usr/bin/python3
"""
Script that prints the mean color of shirts worn
"""

import sys

# Execute code when it runs as a script
if __name__ == "__main__":

    # Define a dictionary to map color names to numerical values
    color_values = {
            "ARSH": 1,
            "BLACK": 2,
            "BLUE": 3,
            "BROWN": 4,
            "CREAM": 5,
            "GREEN": 6,
            "ORANGE": 7,
            "PINK": 8,
            "RED": 9,
            "WHITE": 10,
            "YELLOW": 11,
            }

    # List of colors worn on each day
    colors_per_day = [
            ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
            ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
            ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
            ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
            ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"],
            ]

    # Correct the typo in the colors_per_day list ("BLEW" should be "BLUE")
    for day in colors_per_day:
        for i in range(len(day)):
            if day[i] == "BLEW":
                day[i] = "BLUE"

	# Calculate the total value of colors worn throughout the week
    total_color_value = sum(color_values[color] for day in colors_per_day for color in day)

    # Calculate the mean color value
    mean_color_value = total_color_value / (len(colors_per_day) * len(colors_per_day[0]))

    # Find the color with the closest value to the mean color value
    mean_color = min(color_values, key=lambda color: abs(color_values[color] - mean_color_value))

    # Print the mean color
    print("The mean color of the shirts is:", mean_color)
