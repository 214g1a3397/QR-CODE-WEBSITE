import qrcode
data = "https://www.youtube.com/results?search_query=maggi+recipes"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

img.show()
img.save("qrcode.png")
img.show()
