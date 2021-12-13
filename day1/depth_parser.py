"""
Solution to AOC 2021 day 1
"""
import sys

# Read input file
with open('input.txt') as f:
    sonar_meas = f.readlines()
    sonar_meas = [int(line.rstrip()) for line in sonar_meas]

# Determine increasing or decreasing depth
counter = 0
for i in range(len(sonar_meas)-1):
    if sonar_meas[i+1] > sonar_meas[i]:
        counter += 1

# Count how many times the depth increased
print(f"Depth increased {counter} times")

counter_windowed = 0
# Calculate partial sum of three-measurement windows
for i in range(len(sonar_meas)-3):
    first_partial_sum = sonar_meas[i] + sonar_meas[i+1] + sonar_meas[i+2]
    second_partial_sum = sonar_meas[i+1] + sonar_meas[i+2] + sonar_meas[i+3]
    if second_partial_sum > first_partial_sum:
        counter_windowed += 1

print(f"Windowed measurements increased {counter_windowed} times ")
