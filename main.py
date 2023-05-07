alphabet = []
Text_chiffrer = ""




# Add each letter of the alphabet to the array using a for loop
for letter in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(letter))

print('The encryption key is three')
Text_Claire=input('Give the clear text: ')

Text_Claire = Text_Claire.upper()
for char in Text_Claire:
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
print("Cipher text is : "+Text_chiffrer)