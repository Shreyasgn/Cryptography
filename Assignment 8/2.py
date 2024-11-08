2. Write a python script to take two integer values (number (n) and modulo (m)) from the user and find the modular inverse using extended Euclidean algorithm. 

def extended_euclidean(a, b):
    """
    Extended Euclidean Algorithm
    Returns (gcd, x, y) such that a * x + b * y = gcd
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def modular_inverse(n, m):
    """
    Calculates the modular inverse of n modulo m using Extended Euclidean Algorithm
    Returns the inverse if it exists, or None if it doesn't
    """
    gcd, x, _ = extended_euclidean(n, m)
    if gcd != 1:
        return None  # Modular inverse doesn't exist
    else:
        return x % m

# Get input from the user
n = int(input("Enter the number (n): "))
m = int(input("Enter the modulo (m): "))

# Calculate the modular inverse
inverse = modular_inverse(n, m)

# Print the result
if inverse is None:
    print(f"The modular inverse of {n} modulo {m} does not exist.")
else:
    print(f"The modular inverse of {n} modulo {m} is: {inverse}")
    # Verification
    print(f"Verification: ({n} * {inverse}) mod {m} = {(n * inverse) % m}")
