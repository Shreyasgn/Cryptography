4.  write a python script to break hill cipher (2X2) using known plain text attack. 
	Known Plaintext: "MEET"
	Corresponding Ciphertext: "URRG"


import numpy as np

def letter_to_number(letter):
    return ord(letter) - ord('A')

def number_to_letter(number):
    return chr(number % 26 + ord('A'))

def matrix_mod_inv(matrix, modulus):
    """Calculate the modular inverse of a 2x2 matrix"""
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det % modulus, -1, modulus)
    adjugate = np.array([[matrix[1, 1], -matrix[0, 1]], 
                         [-matrix[1, 0], matrix[0, 0]]])
    return (adjugate * det_inv) % modulus

# Known plaintext and ciphertext
plaintext = "MEET"
ciphertext = "URRG"

# Convert plaintext and ciphertext to number matrices
P = np.array([[letter_to_number(plaintext[0]), letter_to_number(plaintext[2])],
              [letter_to_number(plaintext[1]), letter_to_number(plaintext[3])]])

C = np.array([[letter_to_number(ciphertext[0]), letter_to_number(ciphertext[2])],
              [letter_to_number(ciphertext[1]), letter_to_number(ciphertext[3])]])

# Calculate the key matrix
P_inv = matrix_mod_inv(P, 26)
K = (C @ P_inv) % 26

print("Recovered Key Matrix:")
print(K)

# Verify the key by encrypting the plaintext
def encrypt(plaintext, key):
    result = ""
    for i in range(0, len(plaintext), 2):
        chunk = np.array([letter_to_number(plaintext[i]), 
                          letter_to_number(plaintext[i+1])])
        encrypted = (key @ chunk) % 26
        result += number_to_letter(encrypted[0]) + number_to_letter(encrypted[1])
    return result

encrypted = encrypt(plaintext, K)
print(f"\nVerification:")
print(f"Original Plaintext: {plaintext}")
print(f"Known Ciphertext:   {ciphertext}")
print(f"Encrypted with recovered key: {encrypted}")

if encrypted == ciphertext:
    print("\nSuccess! The recovered key correctly encrypts the plaintext to the known ciphertext.")
else:
    print("\nError: The recovered key does not produce the expected ciphertext.")
    
