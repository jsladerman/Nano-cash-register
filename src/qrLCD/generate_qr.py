import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 3.5,
    border = 8,
)

data = "Test QR Code"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img = img.convert('RGB')
img.save('../resources/qr.bmp')
print('QR Code generated in resources folder')
