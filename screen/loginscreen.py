#Kütüphaneler
import tkinter

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

#Pull Login Data
def pulldata():
    username = input_username.get()
    print("Kullanıcı Adı:",username)
    password = input_password.get() 
    print("Şifre:",password)


button_login = tkinter.Button(text="ENTER",command= pulldata)
button_login.pack()


window.mainloop()