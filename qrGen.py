import qrcode

def createQR_Default(content):
    img = qrcode.make(content)
    type(img)
    path = "GeneratedQR.png"
    img.save(path)
    return path

def createQR_Advanced(content, bgColor = "black", fillColor = "gold", qrSize = 10, borderSize = 4, path = "GeneratedQR.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= qrSize,
        border= borderSize,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fillColor, back_color=bgColor)
    img.save(path)
    return path