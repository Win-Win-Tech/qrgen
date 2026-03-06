import qrcode

# Text to encode
data = "QR16B5Z13KAW"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size of the QR code (1 = smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("Eighth Floor.png")

print("QR code generated and saved as qrcode.png")
