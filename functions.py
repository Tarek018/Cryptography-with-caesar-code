def caesar_code(Text):
    alphabet = []
    # Add each letter of the alphabet to the array using a for loop
    for letter in range(ord('A'), ord('Z') + 1):
        alphabet.append(chr(letter))
    Text_chiffrer = ""
    for char in Text:
        i=0
        for ch in alphabet:
            if char == ch and char =="X":
                Text_chiffrer = Text_chiffrer + alphabet[0]    
                break
            else:
                if char == ch and char == 'Y':
                    Text_chiffrer = Text_chiffrer + alphabet[1]
                    break
                else:
                    if char == ch and char == 'Z':
                        Text_chiffrer = Text_chiffrer + alphabet[2]
                        break
                    else:
                        if char == ch:
                            Text_chiffrer = Text_chiffrer + alphabet[i+3]
            i=i+1     
    return Text_chiffrer