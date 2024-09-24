# Program to encrypt a message encoded using Vigenere Cypher. 
# 
# This program takes user input of a message that the user would like to encrypt using vignere cypher. 
# Program then takes user input and encrypts the message using the key 'leg' as specified in the requirements of the
# assignment. Code is editale to hard code a word for encryption but i thought it more flexible to allow the user to 
# choose a word of their choice. Keeping to the requirements this word is 'explanation'. It 
# then outputs the encrypted word as well as the 'extended key' used for encryption.




def vigenere_encrypt(plaintext, key):
    key = key.lower()
    key_length = len(key)
    plaintext_length = len(plaintext)

    first = key * (plaintext_length // key_length)
    second = key[:plaintext_length % key_length]

    # Extend the key to match the plaintext length
    extended_key = first + second

    encrypted_text = ""

    for i in range(plaintext_length):
        text_char = plaintext[i]
        key_char = extended_key[i]

        if text_char.islower():
            shift = ord(key_char) - ord('a')
            encrypted_char = chr((ord(text_char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += text_char

    return encrypted_text, extended_key, first, second  
    # Return both encrypted_text and extended_key

# Define the plaintext and key

plaintext = message = input("Enter the message to encrypt: ")
key = "leg"

# Encrypt the message
encrypted_message, extended_key, first, second = vigenere_encrypt(plaintext, key)  # Unpack the returned values
print("---------------------------------------------------------")
print("Encrypted Message:", encrypted_message)
print("---------------------------------------------------------")
#print ("first:", first )
#print("second:", second)
print("Extended Key Used:", extended_key)  # Now you can print extended_key