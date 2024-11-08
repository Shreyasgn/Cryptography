3. Write a report on attacks on LFSR. Explain any one attack in detail.

import random

def generate_random_binary(length):
    """Generate a random binary sequence of specified length."""
    return ''.join(random.choice('01') for _ in range(length))

def find_repeating_subsequence(binary_string):
    """
    Check if any subsequence repeats within the binary string.
    Returns a tuple (bool, str) where bool indicates if a repeat was found,
    and str is the repeating subsequence (or empty string if none found).
    """
    n = len(binary_string)
    for length in range(2, n // 2 + 1):  # Check subsequences up to half the string length
        for i in range(n - length + 1):
            subsequence = binary_string[i:i+length]
            if binary_string.count(subsequence) > 1:
                return True, subsequence
    return False, ""

# Generate a random 100-bit binary number
binary_sequence = generate_random_binary(100)

print("Generated 100-bit binary sequence:")
print(binary_sequence)

# Check for repeating subsequences
has_repeat, repeating_sequence = find_repeating_subsequence(binary_sequence)

if has_repeat:
    print(f"\nRepeating subsequence found: {repeating_sequence}")
    print(f"Length of repeating subsequence: {len(repeating_sequence)}")
else:
    print("\nNo repeating subsequences found.")

# Additional analysis
print(f"\nNumber of 0s: {binary_sequence.count('0')}")
print(f"Number of 1s: {binary_sequence.count('1')}")
