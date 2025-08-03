import qrcode as qr

def createQR(content):
    img = qr.make(content)
    type(img)
    path = "GeneratedQR.png"
    img.save(path)
    return path