#!/usr/bin/python3
"""
Script that prints which color is mostly worn throughout the week
"""

from collections import Counter


# Execute code when it runs as a script
if __name__ == "__main__":

    # List of colors worn on each day
    colors_per_day = [
        ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
        ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
        ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"],
    ]

    # Correct the typo in the colors_per_day list ("BLEW" should be "BLUE")

    for day in colors_per_day:
        for i in range(len(day)):
            if day[i] == "BLEW":
                day[i] = "BLUE"

    # Flatten the list of colors to count each occurrence
    all_colors = [color for day in colors_per_day for color in day]

    # Count the occurrences of each color
    color_counts = Counter(all_colors)

    # Find the color with the maximum count (most worn color)
    most_worn_color = color_counts.most_common(1)[0][0]

    # Print the most worn color
    print("The most worn color throughout the week is:", most_worn_color)
