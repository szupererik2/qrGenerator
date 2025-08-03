import qrGen as qr
import os
content = input("Enter the qr content : ")
path = qr.createQR(content)
os.startfile(path)