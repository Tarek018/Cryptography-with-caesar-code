from tkinter import *
from tkinter import ttk,filedialog,messagebox,simpledialog
import re
from functions import caesar_code
import subprocess



enable_btn =DISABLED 
key = 0
plain_text = ''
file_validty = False
chiffre_btn:any
key_button:any
decrypt_btn:any
encrypt_btn:any


def open_file():
    global key_button
    global chiffre_btn
    file_path = filedialog.askopenfilename()
    text = ''
    global file_validty
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            # Check if the file contains numbers
            if re.search(r'\d', text):
                messagebox.showwarning("Alert", "The file contains numbers!\nPlease try again.")
                key_button.config(state=DISABLED)
                chiffre_btn.config(state=DISABLED)
            else:
                text = text.upper()
                text = re.sub(r'\s', '', text)
                print(text)
                global plain_text
                plain_text = text
                key_button.config(state=ACTIVE)

            
def enter_key():
    global key_button
    global chiffre_btn
    number = simpledialog.askinteger("Enter a Number", "Please enter a number:")
    print(number)
    if(number > 25 or number < 1):
        messagebox.showwarning("Alert", "The key should be between 1 and 25\nPlease try again.")
        chiffre_btn.config(state=DISABLED)
    else:
        global key
        key = number
        chiffre_btn.config(state=ACTIVE)

def encrypt_text():
    global key_button
    global chiffre_btn
    cipher_text = caesar_code(plain_text, key)
    print(cipher_text)    
    new_file_path = "encrypted_file.txt"
    with open(new_file_path, 'w') as file:
        # Write content to the file
        file.write(cipher_text)
        subprocess.Popen(['notepad.exe',new_file_path])



def page1():
    global key_button
    global chiffre_btn
    global encrypt_btn
    global decrypt_btn
    encrypt_btn.config(state=DISABLED)
    decrypt_btn.config(state=ACTIVE)


    select_button = Button(root, text="Select File", command=open_file,height=5, width=20, cursor="hand2")
    select_button.pack(padx=50, pady=50)

    key_button = Button(root, text="Enter the key", command=enter_key, state= DISABLED, height=5, width=20, cursor="hand2")
    key_button.pack(padx=50, pady=50)

    chiffre_btn = Button(root, text="Encrypt", command=encrypt_text, state= DISABLED,height=5, width=20, cursor="hand2")
    chiffre_btn.pack(padx=50, pady=50)

def page2():
    global encrypt_btn
    global decrypt_btn
    encrypt_btn.config(state=ACTIVE)
    decrypt_btn.config(state=DISABLED)


    select_button = Button(root, text="Select File", command=open_file,height=5, width=20, cursor="hand2")
    select_button.pack(padx=50, pady=50)

    key_button_decrypt = Button(root, text="Enter the key", command=enter_key, state= DISABLED, height=5, width=20, cursor="hand2")
    key_button_decrypt.pack(padx=50, pady=50)

    decrypt_btn = Button(root, text="Decrypt", command=encrypt_text, state= DISABLED,height=5, width=20, cursor="hand2")
    decrypt_btn.pack(padx=50, pady=50)


root = Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())
encrypt_btn = Button(root, text="Encrypt", command=page1,state=NORMAL, height=5, width=20, cursor="hand2")
encrypt_btn.pack(padx=50, pady=50,side="left")
decrypt_btn = Button(root, text="Decrypt", command=page2,state=NORMAL, height=5, width=20, cursor="hand2")
decrypt_btn.pack(padx=50, pady=50,side="left")


root.mainloop()
