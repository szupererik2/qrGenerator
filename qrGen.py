import qrcode as qr
import os

img = qr.make("https://www.youtube.com/")
type(img)
img.save("GeneratedQR.png")