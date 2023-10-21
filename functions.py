import string

def caesar_code(Text,key):
    alphabet = []
    # Add each letter of the alphabet to the array using a for loop
    for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))

    Text_chiffrer = ""

    for char in Text:
        i=0
        alphabet = string.ascii_lowercase
        char = char.lower()
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index+key) % 26
            Text_chiffrer = Text_chiffrer + alphabet[new_index]    
        else:
            return -1  # Character is not in the alphabet
    return Text_chiffrer