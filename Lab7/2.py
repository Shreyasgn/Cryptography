2. Write a Python script to encrypt double columnar transposition. 
def columnar_transposition(message, keyword):
   
    message = ''.join(message.split()).upper()
    keyword = ''.join(keyword.split()).upper()
    
    column_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    num_rows = -(-len(message) // len(keyword))  
    message += 'X' * (num_rows * len(keyword) - len(message))
    grid = [[''] * len(keyword) for _ in range(num_rows)]
    
    # Fill the grid with the message
    index = 0
    for row in range(num_rows):
        for col in range(len(keyword)):
            grid[row][col] = message[index]
            index += 1
    
    # Read off the columns according to the keyword order
    ciphertext = ''
    for col in column_order:
        ciphertext += ''.join(grid[row][col] for row in range(num_rows))
    
    return ciphertext

def double_columnar_transposition_encrypt(message, keyword1, keyword2):
    # First transposition
    first_encryption = columnar_transposition(message, keyword1)
    
    # Second transposition
    second_encryption = columnar_transposition(first_encryption, keyword2)
    
    return second_encryption
message = input("Enter the message to encrypt: ")
keyword1 = input("Enter the first keyword for encryption: ")
keyword2 = input("Enter the second keyword for encryption: ")

encrypted_message = double_columnar_transposition_encrypt(message, keyword1, keyword2)
print(f"Encrypted message: {encrypted_message}")
