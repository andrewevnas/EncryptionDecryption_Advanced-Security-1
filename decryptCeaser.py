# Program to decrypt a message encoded using Ceaser Cypher. 
# 
# This program takes user input of a Ceaser 
# encrypted message and tests multiple shifts to decrypt the passage. Once all shifts in the designated range
# have been tested, program looks in each decryption for commonly used english words and uses this information
# to output the (most likely) shift value as well as the passage that it thinks is the correct decryption



def decrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            result += char
    
    return result

# List of common English words for validation
common_words = ["the", "and", "is", "in", "it", "you", "that", "he", "was", "for", "on", "are", "as", "with", "his", "they", "at", "be", "this", "from"]

def is_english(text):
    words = text.split()
    match_count = 0
    
    
    # Count how many common English words are in the decrypted text
    
    for word in words:
        if word.lower() in common_words:
            match_count += 1
    
    return match_count

# Encrypted text
encrypted_text = input("Enter the message to decrypt: ")

# Store the best guess and its shift value
best_shift = None
best_decryption = ""
max_matches = 0

# Try all possible shifts (1 to 25)
for shift in range(1, 26):
    decrypted_text = decrypt(encrypted_text, shift)
    matches = is_english(decrypted_text)
    
    # If the current decryption has more English words, update the best guess
    if matches > max_matches:
        best_shift = shift
        best_decryption = decrypted_text
        max_matches = matches

# Output the best guess
if best_shift:
    print("---------------------------------------------------------")
    print(f"The correct shift is likely: {best_shift}")
    print("---------------------------------------------------------")
    print(f"Decrypted message: {best_decryption}")
else:
    print("Could not determine the correct shift.")
