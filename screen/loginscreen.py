#Libraries
import tkinter
import time

#Screen
window = tkinter.Tk()
window.title("Login Screen")
window.config(padx=30, pady=30)

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

def pulldata():
    for i in range(len(line)):
        if input_username.get() in line[i] :
            print(line[i])
        else:
            print("olmuyor")
            print(line[i])

#New Note
def newnote():
    global input_yournote
    text_yournote = tkinter.Label(text="Welcome! , what is your note?")
    text_yournote.pack()
    input_yournote = tkinter.Entry(width=20)
    input_yournote.pack()
 
#Create Key For New Note 
    def createnewkey() :
        global input_username
        if input_username == "" :
            print("please add username")
            time.sleep(1)
        else :
            newnote = input_yournote.get()
            with open("C:\\Users\\baris\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\qrsystemfiles\\toberead.txt", 'a') as dosya:
                dosya.write(f"{input_username.get()},{newnote}\n")
            print("veriler kaydedildi , keyin qr kod olarak dosya dizininde!")
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