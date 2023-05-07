alphabet = []

dictionnaire = {}

Text_chiffrer = ""

espace = {}

space_indices = []



# Ajouter chaque lettre de l'alphabet au tableau en utilisant une boucle for
for letter in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(letter))

# Afficher le tableau
print('La cle de chiffrement est trois')
Text_Claire=input('donner le text claire : ')
i=0
# print(alphabet)
Text_Claire = Text_Claire
for char in Text_Claire.upper():
    i=0
    for letter in alphabet:
        if letter == char:
            dictionnaire[char]=i
        i=i+1

for j in range(len(Text_Claire)):
    if Text_Claire[j] == " ":
        space_indices.append(j)

for key,value in dictionnaire.items():
    print(alphabet[value] )
    if alphabet[value] == 'X':
         Text_chiffrer = Text_chiffrer + alphabet[0]
    else:
         if alphabet[value] == 'Y':
             Text_chiffrer = Text_chiffrer + alphabet[1]
         else:
             if alphabet[value] == 'Z':
                 Text_chiffrer = Text_chiffrer + alphabet[2]
             else:
                Text_chiffrer = Text_chiffrer + alphabet[value+3]
    
print(Text_chiffrer)