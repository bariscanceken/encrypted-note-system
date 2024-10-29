<<<<<<< HEAD
#main libraries
import tkinter
import time
import hashlib
import random
import qrcode
import os

# Files Way
base_dir = os.path.dirname(os.path.abspath(__file__))
path_image = os.path.join(base_dir, 'png.png')
path_toberead = os.path.join(base_dir, 'toberead.txt')
path_userdatakey = os.path.join(base_dir, 'userdata.txt')
path_notesqrkey = os.path.join(base_dir, 'notesqrkey')



#Screen
window = tkinter.Tk()
window.title("Login Screen")
window.config(padx=30, pady=30)
image = tkinter.PhotoImage(file=path_image)
image_label = tkinter.Label(window, image=image)
image_label.pack()

#UI
text_username = tkinter.Label(text="Enter Your User Name: ")
text_username.pack()
input_username = tkinter.Entry(width=20)
input_username.pack()
text_key = tkinter.Label(text="Enter Your Key: ")
text_key.pack()
input_key = tkinter.Entry(width=20)
input_key.pack()

#for decrypt pull data
def pulldata():
    for i in range(len(line)):
        if input_username.get() == line[i].split(',')[0] and input_key.get() in line2[i] and len(input_key.get()) == 64 :
            decrypt = line[i]
            text_decrypt = tkinter.Label(text=decrypt)
            text_decrypt.pack()
            return 
    text_wrongmatch = tkinter.Label(text="wrong key and username match!") 
    text_wrongmatch.pack()

#New Note
def newnote():
    global input_yournote
    text_yournote = tkinter.Label(text="welcome! , what is your note?")
    text_yournote.pack()
    input_yournote = tkinter.Entry(width=20)
    input_yournote.pack()
 
#Create Key For New Note 
    def createnewkey() :
        global x
        global input_username
        if input_username.get() == "" :
            print("please add username")
            time.sleep(1)
        else :
            newnote = input_yournote.get()
            with open(path_toberead, 'a') as dosya:
                dosya.write(f"{input_username.get()},{newnote}\n")
            print("your key is saved as qr!")
            x = 1
    button_noteokey = tkinter.Button(text="Create Key!",command= createnewkey)
    button_noteokey.pack()

#File System
with open(path_toberead, 'r') as dosya:
    line = dosya.readlines()
    if line:  
        last_line = line[-1]
    else:
        last_line = None
with open(path_userdatakey, 'r') as dosya:
    line2 = dosya.readlines()

#Login Buttons
button_login = tkinter.Button(text="Enter",command= pulldata)
button_login.pack()
button_register = tkinter.Button(text="New Note",command= newnote)
button_register.pack()
window.mainloop()

#Take the Thing to Encrypt and Add One of the Random Letters
while x == 1: 
    convertuserdata = last_line
    private = ["h", "g"]
    letters = [] 
    letters.append(random.choice(private))

    # Encryption Algorithm (Sezar and Hash , Random)
    def hmletters():
        global convertuserdata
        global letters
        letters = [random.choice(private)] 
        for l in convertuserdata:
            letters.append(l)
    hmletters()
    funcsha256 = hashlib.sha256()
    before_generate = ""
    for letter in letters:
        funcsha256.update(letter.encode())
        before_generate += funcsha256.hexdigest() 
    funcsha256.update(before_generate.encode())
    forqr = funcsha256.hexdigest()
    print(forqr)

    #Qr Formation and Where to Save
    with open(path_userdatakey, 'a') as dosya:
        dosya.write(f"{forqr}\n")
    fornamedif = line[-1].split(',')[0]
    qr = qrcode.QRCode(
        version=8, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)
    qr.add_data(forqr)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")
    file_path = os.path.join(path_notesqrkey, f"userdata{fornamedif}.png")
    img.save(file_path)
=======
#main libraries
import tkinter
import time
import hashlib
import random
import qrcode
import os

# Files Way
base_dir = os.path.dirname(os.path.abspath(__file__))
path_image = os.path.join(base_dir, 'png.png')
path_toberead = os.path.join(base_dir, 'toberead.txt')
path_userdatakey = os.path.join(base_dir, 'userdata.txt')
path_notesqrkey = os.path.join(base_dir, 'notesqrkey')



#Screen
window = tkinter.Tk()
window.title("Login Screen")
window.config(padx=30, pady=30)
image = tkinter.PhotoImage(file=path_image)
image_label = tkinter.Label(window, image=image)
image_label.pack()

#UI
text_username = tkinter.Label(text="Enter Your User Name: ")
text_username.pack()
input_username = tkinter.Entry(width=20)
input_username.pack()
text_key = tkinter.Label(text="Enter Your Key: ")
text_key.pack()
input_key = tkinter.Entry(width=20)
input_key.pack()

#for decrypt pull data
def pulldata():
    for i in range(len(line)):
        if input_username.get() == line[i].split(',')[0] and input_key.get() in line2[i] and len(input_key.get()) == 64 :
            decrypt = line[i]
            text_decrypt = tkinter.Label(text=decrypt)
            text_decrypt.pack()
            return 
    text_wrongmatch = tkinter.Label(text="wrong key and username match!") 
    text_wrongmatch.pack()

#New Note
def newnote():
    global input_yournote
    text_yournote = tkinter.Label(text="welcome! , what is your note?")
    text_yournote.pack()
    input_yournote = tkinter.Entry(width=20)
    input_yournote.pack()
 
#Create Key For New Note 
    def createnewkey() :
        global x
        global input_username
        if input_username.get() == "" :
            print("please add username")
            time.sleep(1)
        else :
            newnote = input_yournote.get()
            with open(path_toberead, 'a') as dosya:
                dosya.write(f"{input_username.get()},{newnote}\n")
            print("your key is saved as qr!")
            x = 1
    button_noteokey = tkinter.Button(text="Create Key!",command= createnewkey)
    button_noteokey.pack()

#File System
with open(path_toberead, 'r') as dosya:
    line = dosya.readlines()
    if line:  
        last_line = line[-1]
    else:
        last_line = None
with open(path_userdatakey, 'r') as dosya:
    line2 = dosya.readlines()

#Login Buttons
button_login = tkinter.Button(text="Enter",command= pulldata)
button_login.pack()
button_register = tkinter.Button(text="New Note",command= newnote)
button_register.pack()
window.mainloop()

#Take the Thing to Encrypt and Add One of the Random Letters
while x == 1: 
    convertuserdata = last_line
    private = ["h", "g"]
    letters = [] 
    letters.append(random.choice(private))

    # Encryption Algorithm (Sezar and Hash , Random)
    def hmletters():
        global convertuserdata
        global letters
        letters = [random.choice(private)] 
        for l in convertuserdata:
            letters.append(l)
    hmletters()
    funcsha256 = hashlib.sha256()
    before_generate = ""
    for letter in letters:
        funcsha256.update(letter.encode())
        before_generate += funcsha256.hexdigest() 
    funcsha256.update(before_generate.encode())
    forqr = funcsha256.hexdigest()
    print(forqr)

    #Qr Formation and Where to Save
    with open(path_userdatakey, 'a') as dosya:
        dosya.write(f"{forqr}\n")
    fornamedif = line[-1].split(',')[0]
    qr = qrcode.QRCode(
        version=8, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)
    qr.add_data(forqr)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")
    file_path = os.path.join(path_notesqrkey, f"userdata{fornamedif}.png")
    img.save(file_path)
>>>>>>> 5c708b6bc23dc8b4a5a3de0017e8796eed334e83
    break