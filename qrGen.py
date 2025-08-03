import qrcode

def createQR_Default(content):
    img = qrcode.make(content)
    type(img)
    path = "GeneratedQR.png"
    img.save(path)
    return path

def createQR_Advanced(content):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="gold", back_color="black")
    path = "GeneratedQR.png"
    img.save(path)
    return path