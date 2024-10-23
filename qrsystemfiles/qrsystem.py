#Kütüphaneler
import qrcode
import os
import time

#Değişken Atamaları
with open("C:\\Users\\baris\\OneDrive\\Masaüstü\\qr-login-system-to-user-data\\toberead.txt", 'r') as dosya:
    line = dosya.readlines()
    last_line = (line[-1].strip())

#Fonksiyonun Çalıştığı Kısım
def func_start() :
        willbe = int(last_line) + 1
        with open("C:\\Users\\baris\\OneDrive\\Masaüstü\\qr-login-system-to-user-data\\toberead.txt", 'a') as dosya:
            dosya.write(f"{willbe}\n")
            print(line)

func_start()

#Qr Kodun Oluşturulması
qr = qrcode.QRCode(
    version=8, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4)

qr.add_data(last_line)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")

#Konum
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, f"qrcode{last_line}.png")

img.save(file_path)

time.sleep(1)

# while not click exit:
# func_start()
