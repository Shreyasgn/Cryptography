4. Write a Python script to encrypt and decrypt Hill cipher

def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) - ord('A') for i in keyword]
    
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            char_num = ord(char) - ord('A')
            keyword_num = keyword_as_int[i % keyword_length]
            encrypted_num = (char_num + keyword_num) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext
message = "She is listening"
keyword = "PASCAL"

encrypted_message = vigenere_encrypt(message, keyword)

print(f"Original message: {message}")
print(f"Keyword: {keyword}")
print(f"Encrypted message: {encrypted_message}")
