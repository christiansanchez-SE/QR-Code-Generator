# Flask: The main class used to create an instance of the web application
# Request: Used to handle incoming data in the form of HTTP requests
# Render_template: Used to render HTML templates
# Send_file: Used to send files to the client
from flask import Flask, request, render_template, send_file
# This is a library used to generate QR codes
import qrcode
# This is a library used to handle image files. 
from PIL import Image

# Creating a QRCode object with the specified parameters
qr = qrcode.QRCode(
    version=15,  # This parameter defines the size of the QR code. A higher number means the QR code can hold more data but will be more complex. Version 15 is quite large and can hold a significant amount of information
    box_size=10,  # This parameter sets the size of each individual box (or "module") in the QR code grid. Here, each box will be 10 pixels by 10 pixels
    border=5  # This parameter sets the thickness of the border around the QR code. A border of 5 means there will be a 5-box-wide white space around the QR code
)

# This is the information you want to encode in the QR code. In this case, it's the URL for YouTube
data = "https://www.youtube.com/"

# Add data to the QR code
qr.add_data(data) # This method adds the data to the QRCode object
qr.make(fit=True) # This method finalizes the QR code configuration. The fit=True parameter ensures that the QR code dimensions are adjusted to fit the amount of data provided

# Create an image from the QR code instance
img = qr.make_image(fill="black", back_color="white") # This method generates an image from the QR code object. The 'fill' parameter sets the color of the QR code itself (black), and the 'back_color' sets the background color (white)

# Save the image to a file
img.save("test.png") # This method saves the generated QR code image to a file named 'test.png'
