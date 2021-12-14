"""
Advent of Code 2021 Day 2 Solutions
"""

# Read input file
x = y = 0
with open('input.txt') as f:
    for line in f:
        direction, length = line.split()
        if direction == "forward":
            x += int(length)
        if direction == "up":
            y -= int(length)
        if direction == "down":
            y += int(length)

# Solutions to part 1
print(f"Final position {(x, y)}")
print(f"x*y product: {x * y}")

# Solve part 2 (new interpretation of the commands)
aim = x = y = 0
with open('input.txt') as f:
    for line in f:
        direction, length = line.split()
        if direction == "forward":
            x += int(length)
            y += (aim * int(length))
        if direction == "up":
            aim -= int(length)
        if direction == "down":
            aim += int(length)

# Solutions to part 2
print(f"Final position {(x,y)}")
print(f"xy product: {x*y}")
