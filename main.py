from tkinter import *
from cryptography.fernet import Fernet
import base64




def encrypt_function():
    enc = []
    word = stitle_text.get("1.0",END)
    key = key_function()
    for i in range(len(word)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(word[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt_funciton():
    word = stitle_text.get("1.0",END)
    dec = []
    enc = base64.urlsafe_b64decode(word).decode()
    key = key_function()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    final_word = "".join(dec)
    stitle_text.delete("1.0",END)
    stitle_text.insert("1.0", final_word)

def key_function():
    global key
    key=mtitle_entry.get()
    return key

def write_to_file():
    title = ntitle_entry.get()
    enc_text = encrypt_function()
    f = open("enc_notes.txt", "a")
    f.write(f"{title}\n{enc_text}\n")
    f.close()


root = Tk()
root.title("Secret Notes")
root.minsize(width=250,height=350)

ntitle_label = Label(text="Enter your title")
ntitle_label.pack()
ntitle_entry = Entry()
ntitle_entry.pack()

stitle_label = Label(text="Enter your secret")
stitle_label.pack()
stitle_text = Text(width=30,height=10)
stitle_text.pack()

mtitle_label = Label(text="Enter master key")
mtitle_label.pack()
mtitle_entry = Entry()
mtitle_entry.pack()

save_enc_button = Button(text="Save & Encrypt",command=lambda:[write_to_file()])
save_enc_button.pack()

decrypt_button = Button(text="Decrypt",command=decrypt_funciton)
decrypt_button.pack()


root.mainloop()