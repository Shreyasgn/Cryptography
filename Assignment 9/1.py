1. Write a python script to get the binary values from the user and perform XOR operation. 

def is_binary(s):
    """Check if a string consists only of '0's and '1's."""
    return set(s) <= {'0', '1'}

def binary_xor(a, b):
    """Perform XOR operation on two binary strings of equal length."""
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def get_binary_input(prompt):
    """Get a valid binary input from the user."""
    while True:
        value = input(prompt)
        if is_binary(value):
            return value
        else:
            print("Invalid input. Please enter a binary number (consisting of only 0s and 1s).")

# Get binary inputs from the user
binary1 = get_binary_input("Enter the first binary number: ")
binary2 = get_binary_input("Enter the second binary number: ")

# Ensure both binary strings are of equal length
max_length = max(len(binary1), len(binary2))
binary1 = binary1.zfill(max_length)
binary2 = binary2.zfill(max_length)

# Perform XOR operation
result = binary_xor(binary1, binary2)

# Print the result
print(f"\nFirst binary number:  {binary1}")
print(f"Second binary number: {binary2}")
print(f"XOR result:           {result}")

# Optional: Convert to decimal for additional context
print(f"\nDecimal equivalents:")
print(f"First number:  {int(binary1, 2)}")
print(f"Second number: {int(binary2, 2)}")
print(f"XOR result:    {int(result, 2)}")
