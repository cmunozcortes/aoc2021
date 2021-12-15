"""
Advent of Code 2021 Day 3
"""

# List holding counters for each bit
ones_counter = [0 for i in range(12)]

# Counter to keep track of lines read
num_lines = 0

# Load input file
report = []
with open("./input.txt") as f:
    for line in f:
        report.append(line.rstrip())
        num_lines += 1
        for i, bit in enumerate(line):
            if bit == '1':
                ones_counter[i] += 1

# `bits` is a list of tuples where the first element is the most common bit
# in that position, and the second element the least common bit.
bits = [('1','0') if ones >= num_lines/2 else ('0','1') for ones in ones_counter]
most_common_bits, least_common_bits = map(list, zip(*bits))
gamma_rate = int(''.join(most_common_bits), 2)
epsilon_rate = int(''.join(least_common_bits), 2)

# Print out solution
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {gamma_rate * epsilon_rate}")

# Solution to part 2
most_common_bits = ''.join(most_common_bits)
print(f"Most common bits: {most_common_bits}")

oxygen_generator_rating = 0
for i in range(len(most_common_bits)):
    if oxygen_generator_rating == 0:
        print(f"\nIteration {i}")
        for binary in report:
            print(f"Comparing {most_common_bits[:-i or None]} with")
            print(f"          {binary}")
            if most_common_bits[:-i or None] == binary[:-i or None]:
                print(f"Matched {binary}")
                oxygen_generator_rating = binary
                break
            else:
                    print(f"No match for {most_common_bits[:-i or None]}")
    else:
        break
