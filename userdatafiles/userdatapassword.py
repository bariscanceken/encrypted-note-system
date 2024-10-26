#Kütüphaneler
import hashlib
import random
import qrcode
import os

# Şifrelenecek Şeyi Al Ve Random Belirli Harflerden Birini Ekle
convertuserdata = input("Oluşturmak İstediğiniz Şifreyi Giriniz: ")
private = ["h", "g"]
letters = [] 
letters.append(random.choice(private))

# Şifreleme Algoritması (Sezar ve Hash , Random)
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

#Qr Oluşumu ve Kaydedilecek Yer
qr = qrcode.QRCode(
    version=8, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4)

qr.add_data(forqr)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "userdata.png")

img.save(file_path)