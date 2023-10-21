from tkinter import *
from tkinter import ttk,filedialog,messagebox,simpledialog
import re
from functions import caesar_code
import subprocess



enable_btn =DISABLED 
key = 0
plain_text = ''


def open_file():
    file_path = filedialog.askopenfilename()
    text = ''
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            # Check if the file contains numbers
            if re.search(r'\d', text):
                messagebox.showwarning("Alert", "The file contains numbers!\nPlease try again.")
            else:
                text = text.upper()
                text = re.sub(r'\s', '', text)
                print(text)
                global plain_text
                plain_text = text
            
def enter_key():
    number = simpledialog.askinteger("Enter a Number", "Please enter a number:")
    print(number)
    if(number > 25 or number < 1):
        messagebox.showwarning("Alert", "The key should be between 1 and 25\nPlease try again.")
    else:
        global key
        key = number
        chiffre_btn.config(state=ACTIVE)

def encrypt_text():
    cipher_text = caesar_code(plain_text, key)
    print(cipher_text)    
    new_file_path = "encrypted_file.txt"
    with open(new_file_path, 'w') as file:
        # Write content to the file
        file.write(cipher_text)
        subprocess.Popen(['notepad.exe',new_file_path])










root = Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

select_button = Button(root, text="Select File", command=open_file)
select_button.pack()

key_button = Button(root, text="Enter the key", command=enter_key)
key_button.pack()

chiffre_btn = Button(root, text="Encrypt", command=encrypt_text, state= enable_btn)
chiffre_btn.pack()





root.mainloop()
