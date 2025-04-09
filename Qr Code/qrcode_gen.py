import qrcode

data = input("Enter text or URL: ").strip()
filename = input("Enter file name (without extension): ").strip()

# Ensure the filename ends with .png
if not filename.lower().endswith('.png'):
    filename += '.png'

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')
