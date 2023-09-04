import qrcode
from PIL import Image

# This is the link that I will use to generate my QR Code, feel free to use any link of your choice
my_link = "https://www.instagram.com/digital_ground_official/"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(my_link)
qr.make(fit=True)

image = qr.make_image(fill="black", back_color="white")
image.save("my_qr_code.png")
Image.open("my_qr_code.png")

# Thank you for watching