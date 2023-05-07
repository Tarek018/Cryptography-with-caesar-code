from functions import caesar_code

print('The encryption key is three')
Text_Claire=input('Give the clear text: ')

# To make all characters uppercase
Text_Claire = Text_Claire.upper()

print("Cipher text is : "+caesar_code(Text_Claire))