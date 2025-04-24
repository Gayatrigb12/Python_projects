import qrcode
from PIL import Image
from datetime import datetime

# Get input from the user
data = input("Enter the data or URL to encode in the QR code: ")
fill_color = input("Enter the fill color (e.g., 'blue', 'red', 'green'): ")
back_color = input("Enter the background color (e.g., 'white', 'black'): ")

# Generate a timestamp-based file name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"qr_{timestamp}.png"

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Generate the image with custom colors
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save the image with a timestamped file name
img.save(f"D:\PYTHON\Python_POC\Python_projects\QR_Gen\QR\{file_name}")

print(f"QR code generated and saved as '{file_name}'")

















# import qrcode
# import qrcode.constants
# from PIL import Image

# qr = qrcode.QRCode(version=1 , error_correction=qrcode.constants.ERROR_CORRECT_H , box_size= 10 , border= 4 )  
# #  function QrCode , in that give params like version of qr , error correction highlevel only , box size and border 

# qr.add_data("https://github.com/Gayatrigb12")
# qr.make(fit=True) # data is comming or not 

# img = qr.make_image(fill_color = "blue" , back_color = "black")

# img.save("qr1.png")


