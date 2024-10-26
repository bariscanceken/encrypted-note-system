#Kütüphaneler
import qrcode
import os

#Değişken Atamaları

with open("C:\\Users\\baris\\OneDrive\\Masaüstü\\haha\\qr-login-system-to-user-data\\qrsystemfiles\\toberead.txt", 'r') as dosya:
    line = dosya.readlines()
    last_line = (line[-1].strip())
    print(last_line)

#Qr Kodun Oluşturulması
qr = qrcode.QRCode(
    version=8, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4)

qr.add_data(last_line)
qr.make(fit=True)
img = qr.make_image(fill_color="purple", back_color="white")

#Konum
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, f"qrcodeuserdata{last_line}.png")

img.save(file_path)


