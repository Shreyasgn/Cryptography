2. Write a Python script to implement RSA algorithm using build in functions (both encryption and decryption)

import random
from sympy import isprime
from math import gcd
from Crypto.Util.number import getPrime, inverse

def generate_keypair(bits=8):
    p = getPrime(bits)  
    q = getPrime(bits) 
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = inverse(e, phi)  
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

public_key, private_key = generate_keypair(bits=8)
print("Public Key:", public_key)
print("Private Key:", private_key)
plaintext = input("Enter a message to encrypt: ")
ciphertext = encrypt(public_key, plaintext)
print("Encrypted Message:", ciphertext)

decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted Message:", decrypted_message)
