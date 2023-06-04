# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

# Find the position of the starting digit
start_index = text.find(':') + 1

# Extract the number by slicing the string
number_str = text[start_index:].strip()

# Convert the extracted value to a floating-point number
number = float(number_str)

# Print the extracted number
print(number)
