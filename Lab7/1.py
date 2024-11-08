1. Write a Python script to encrypt columnar transposition using keyword. 
def columnar_transposition_encrypt(message, keyword):
    # Remove spaces and convert to uppercase
    message = ''.join(message.split()).upper()
    keyword = ''.join(keyword.split()).upper()
    
    # Create the column order based on the keyword
    column_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    
    # Calculate number of rows needed
    num_rows = -(-len(message) // len(keyword))  # Ceiling division
    
    # Pad the message if necessary
    message += 'X' * (num_rows * len(keyword) - len(message))
    
    # Create the grid
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

# Example usage
message = input("Enter the message to encrypt: ")
keyword = input("Enter the keyword for encryption: ")

encrypted_message = columnar_transposition_encrypt(message, keyword)
print(f"Encrypted message: {encrypted_message}")
