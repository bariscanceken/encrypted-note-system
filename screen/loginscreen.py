#Kütüphaneler
import tkinter
import time

userdata = []

#Ekran
window = tkinter.Tk()
window.title("Giriş Ekranı")
window.config(padx=30, pady=30)

#UI
text_username = tkinter.Label(text="Enter Your User Name: ")
text_username.pack()
input_username = tkinter.Entry(width=20)
input_username.pack()
text_password = tkinter.Label(text="Enter Your Password: ")
text_password.pack()
input_password = tkinter.Entry(width=20)
input_password.pack()
text_key = tkinter.Label(text="Enter Your Key: ")
text_key.pack()
input_key = tkinter.Entry(width=20)
input_key.pack()

#Pull Login Data
def pulldata():
    username = input_username.get()
    print("Kullanıcı Adı:",username)
    password = input_password.get() 
    print("Şifre:",password)
    userdata.append(username)
    userdata.append(password)
    print(userdata)

#Register
def newuser():
    global input_registerusername
    global input_registerpassword
    text_registerusername = tkinter.Label(text="Welcome! , what is your username?")
    text_registerusername.pack()
    input_registerusername = tkinter.Entry(width=20)
    input_registerusername.pack()
    text_registerpassword = tkinter.Label(text="Create a Password")
    text_registerpassword.pack()
    input_registerpassword = tkinter.Entry(width=20)
    input_registerpassword.pack()

#Register Verilerini Gönder
    def createnewuserkey() :
        registerusername = input_registerusername.get()
        registerpassword = input_registerpassword.get()
        with open("C:\\Users\\baris\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\screen\\registerdata.txt", 'a') as dosya:
            dosya.write(f"{registerusername}\n{registerpassword}\n\n")
        print("veriler kaydedildi , keyin qr kod olarak dosya dizininde!")
        time.sleep(3)
        exit()

    button_registerokey = tkinter.Button(text="Create Key!",command= createnewuserkey)
    button_registerokey.pack()

#Login Buttonları
button_login = tkinter.Button(text="ENTER",command= pulldata)
button_login.pack()
button_register = tkinter.Button(text="Register",command= newuser)
button_register.pack()
window.mainloop()