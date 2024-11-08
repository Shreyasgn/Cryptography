3. Write a Python script to implement RSA algorithm with out using build in functions (both encryption and decryption)

import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_large_prime(start=100, end=200):
    prime = random.randint(start, end)
    while not is_prime(prime):
        prime = random.randint(start, end)
    return prime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    t, newt = 0, 1
    r, newr = phi, e
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError("No modular inverse exists")
    if t < 0:
        t = t + phi
    return t

def generate_keypair():
    p = generate_large_prime()
    q = generate_large_prime()
    while q == p:
        q = generate_large_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Generate RSA key pairs
public_key, private_key = generate_keypair()
print("Public Key:", public_key)
print("Private Key:", private_key)

# Input plaintext message
plaintext = input("Enter a message to encrypt: ")
ciphertext = encrypt(public_key, plaintext)
print("Encrypted Message:", ciphertext)

# Decrypt the message
decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted Message:", decrypted_message)
