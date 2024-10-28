#Libraries
import tkinter
import time

#Screen
window = tkinter.Tk()
window.title("Login Screen")
window.config(padx=30, pady=30)
image = tkinter.PhotoImage(file="C:\\Users\\baris\\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\screen\\png.png")
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
with open("C:\\Users\\baris\\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\qrsystemfiles\\toberead.txt", 'r') as dosya:
    line = dosya.readlines()

with open("C:\\Users\\baris\\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\userdatafiles\\userdata.txt", 'r') as dosya:
    line2 = dosya.readlines()

def pulldata():

    def wrong():
        text_wrongmatch = tkinter.Label(text="wrong key and username match!") 
        text_wrongmatch.pack()
    
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
        global input_username
        if input_username.get() == "" :
            print("please add username")
            time.sleep(1)
        else :
            newnote = input_yournote.get()
            with open("C:\\Users\\baris\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\qrsystemfiles\\toberead.txt", 'a') as dosya:
                dosya.write(f"{input_username.get()},{newnote}\n")
            print("your key is saved as qr!")
            time.sleep(2)
            exit()

    button_noteokey = tkinter.Button(text="Create Key!",command= createnewkey)
    button_noteokey.pack()

#Login Buttons
button_login = tkinter.Button(text="Enter",command= pulldata)
button_login.pack()
button_register = tkinter.Button(text="New Note",command= newnote)
button_register.pack()
window.mainloop()