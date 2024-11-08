5. Write a Python script to perform Kasiski test. 

import re
from collections import defaultdict
from math import gcd
from functools import reduce

def find_repeated_sequences(ciphertext, min_length=3):
    sequences = defaultdict(list)
    for i in range(len(ciphertext) - min_length + 1):
        seq = ciphertext[i:i + min_length]
        for j in range(i + min_length, len(ciphertext) - min_length + 1):
            if ciphertext[j:j + min_length] == seq:
                sequences[seq].append(j - i)
    return sequences

def kasiski_test(ciphertext, min_length=3):
    sequences = find_repeated_sequences(ciphertext, min_length)
    distances = []
    for seq, positions in sequences.items():
        if len(positions) > 1:
            print(f"Sequence '{seq}' found with distances: {positions}")
            distances.extend(positions)
    
    if not distances:
        print("No repeated sequences found.")
        return None

    keyword_length = reduce(gcd, distances)
    print(f"Estimated keyword length: {keyword_length}")
    return keyword_length

ciphertext = input("Enter the ciphertext: ").upper()
ciphertext = re.sub(r'[^A-Z]', '', ciphertext)

kasiski_test(ciphertext)
