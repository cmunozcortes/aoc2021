"""
Solution to AOC 2021 day 1
"""
# Read input file
with open('input.txt') as f:
    sonar_meas = f.readlines()
    sonar_meas = [line.rstrip() for line in sonar_meas]

# Determine increasing or decreasing depth
counter = 0
for i in range(len(sonar_meas)-1):
    if int(sonar_meas[i+1]) > int(sonar_meas[i]):
        counter += 1

# Count how many times the depth increased
print(counter)
