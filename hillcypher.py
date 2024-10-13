import numpy as np

# Function to convert letters to numbers 
def letter_to_number(char):
    return ord(char.upper()) - ord('A')

# Function to convert numbers back to letters
def number_to_letter(number):
    return chr((number % 26) + ord('A'))

# Function to encrypt the plaintext 
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    
    # Make sure the plaintext length is even
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding X
    
    encrypted_text = ""
    
    for i in range(0, len(plaintext), 2):
        # Convert each pair of characters to numbers
        vector = [letter_to_number(plaintext[i]), letter_to_number(plaintext[i + 1])]
        # Multiply the key matrix with the vector
        result_vector = np.dot(key_matrix, vector) % 26
        # Convert numbers back to letters and add to ciphertext
        encrypted_text += number_to_letter(result_vector[0]) + number_to_letter(result_vector[1])
    
    return encrypted_text

# Function to decrypt the ciphertext using the inverse of the key matrix
def hill_decrypt(ciphertext, key_matrix):
    # Find the modular inverse of the key matrix
    det = int(np.round(np.linalg.det(key_matrix))) 
    det_inv = pow(det, -1, 26)  
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26 
    inverse_key_matrix = (det_inv * adjugate) % 26
    
    decrypted_text = ""
    
    for i in range(0, len(ciphertext), 2):
        # Convert each pair of characters to numbers
        vector = [letter_to_number(ciphertext[i]), letter_to_number(ciphertext[i + 1])]
        # Multiply the inverse key matrix with the vector
        result_vector = np.dot(inverse_key_matrix, vector) % 26
        # Convert numbers back to letters and add to plaintext
        decrypted_text += number_to_letter(result_vector[0]) + number_to_letter(result_vector[1])
    
    # Remove padding 'X' if  added
    return decrypted_text.rstrip('X')

# Example key matrix (2x2)
key_matrix = np.array([[3, 3], [2, 5]])

# Example encryption and decryption, show how it worsk
plaintext = "HELLO"
ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted_text = hill_decrypt(ciphertext, key_matrix)

print("Example encryption and decryption:")
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)

# user choice encrypt or decrypt
choice = input("\nEnter '1' to encrypt your own word or '2' to decrypt your own word: ")

if choice == '1':
    # encrypt
    user_plaintext = input("\nEnter the word you want to encrypt: ").upper()
    
    
    if len(user_plaintext) % 2 != 0:
        print("\nInput length is odd, adding 'X' to the end for encryption.")
        user_plaintext += 'X'
    
    user_ciphertext = hill_encrypt(user_plaintext, key_matrix)
    print("\nEncrypted text:", user_ciphertext)

elif choice == '2':
    #decrypt
    user_ciphertext = input("\nEnter the word you want to decrypt: ").upper()
    
    
    if len(user_ciphertext) % 2 != 0:
        print("\nInput length is odd, adding 'X' to the end for decryption.")
        user_ciphertext += 'X'
    
    user_decrypted_text = hill_decrypt(user_ciphertext, key_matrix)
    print("\nDecrypted text:", user_decrypted_text)

else:
    print("\nInvalid choice. Please enter '1' for encryption or '2' for decryption.")

