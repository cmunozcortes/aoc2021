"""
Advent of Code 2021 Day 3
"""
def find_most_and_least_common_bits(binary_strings, bit_position):
    """
    Finds the most and least common bits at a particular bit location throughout
    a list of binary strings

    Keyword arguments:
    binary_strings -- a list of binary strings
    bit_position -- the ith-position where the most common and least common
        bits need to be searched
    """
    ones = zeros = 0
    most_common_bit = None
    least_common_bit = None
    for binary in binary_strings:
        if binary[bit_position] == '1':
            ones += 1
        else:
            zeros += 1
    if (ones > zeros) or (ones == zeros):
        most_common_bit = 1
        least_common_bit = 0
    else:
        most_common_bit = 0
        least_common_bit = 1
    return (most_common_bit, least_common_bit)

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
print("Part 1:")
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumption: {gamma_rate * epsilon_rate}")

"""
Part 2
"""
# Make copies of the original report. We'll mutate these in place as we begin to
# filter the numbers that match the criteria for the oxygen generator rating and
# the co2 scrubber rating according to the puzzle description.
o2_gen_list = report[:]
co2_scrub_list = report[:]

# Loop over all bits
for i in range(len(report[0])):

    # Determine the most and least common digits in the ith-bit
    mc_bit, _ = find_most_and_least_common_bits(o2_gen_list, i)
    _, lc_bit = find_most_and_least_common_bits(co2_scrub_list, i)

    # Filter numbers with `bit` in bit position `i`
    if len(o2_gen_list) > 1:
        o2_gen_list[:] = [number for number in o2_gen_list
                if int(number[i]) == mc_bit]
    if len(co2_scrub_list) > 1:
        co2_scrub_list[:] = [number for number in co2_scrub_list
                if int(number[i]) == lc_bit]

# Each list should have only 1 element at this point
o2_generator_rating = o2_gen_list.pop()
co2_scrubber_rating = co2_scrub_list.pop()

print("\nPart 2:")
print(f"O2 rating: {int(o2_generator_rating, 2)}")
print(f"CO2 rating: {int(co2_scrubber_rating, 2)}")
life_support_rating = int(o2_generator_rating, 2) * \
                      int(co2_scrubber_rating, 2)
print(f"Submarine life support rating: {life_support_rating}")
