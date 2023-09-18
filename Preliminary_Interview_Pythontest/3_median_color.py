#!/usr/bin/python3
"""
Script that prints the median color
"""

import sys
from collections import Counter

# Execute code when it runs as a script
if __name__ == "__main__":

    # List of color for each day of the week
    colors_per_day = [
        ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
        ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
        ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
    ]


    # Correct the typo in the colors_per_day list ("BLEW" should be "BLUE")

    for day in colors_per_day:
        for i in range(len(day)):
            if day[i] == "BLEW":
                day[i] = "BLUE"

    # Flatten the list of colors for the week
    all_colors = [color for day in colors_per_day for color in day]

    # Count the occurrences of each color
    color_counts = Counter(all_colors)

    # Find the color with the median count
    median_color = color_counts.most_common()[len(color_counts) // 2][0]

    print(f"The median color is: {median_color}")
