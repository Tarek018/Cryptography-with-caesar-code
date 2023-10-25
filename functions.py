import string

def caesar_code(Text,key):
    alphabet = []
    # Add each letter of the alphabet to the array using a for loop
    for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))

    Text_chiffrer = ""

    print(Text)
    for char in Text:
        i=0
        alphabet = string.ascii_lowercase
        char = char.lower()
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index+key) % 26
            Text_chiffrer = Text_chiffrer + alphabet[new_index]    
        else:
            if char == ' ':
                Text_chiffrer = Text_chiffrer + ' '
            else:
                return -1  # Character is not in the alphabet
    return Text_chiffrer

def decrypte_caesar_code(Text):
    alphabet = []
    # Add each letter of the alphabet to the array using a for loop
    for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))
    
    k = 0
    new_file_path = "decrypted_file.txt"
    plainText = ''


    for k in range(26):
        plainText = plainText + '\n'
        plainText = plainText + '- Pour la cle='+str(k)+':\n'
        for char in Text:
            alphabet = string.ascii_lowercase
            char = char.lower()
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index - k) % 26
                plainText = plainText + alphabet[new_index]   
            else:
                if char == ' ':
                    plainText = plainText + ' '
                else:
                    return -1  # Character is not in the alphabet

        k=k+1  # Character is not in the alphabet
    return plainText
