import re

# Read the file
filename = 'regex_sum_42.txt'
with open(filename) as file:
    text = file.read()

# Find all numbers using regular expressions
numbers = re.findall('[0-9]+', text)

# Convert the extracted strings to integers and calculate the sum
total_sum = sum(int(number) for number in numbers)

# Print the sum
print("Sum:", total_sum)
