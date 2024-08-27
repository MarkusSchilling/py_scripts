# This script can be run in the terminal, command prompt, or another environment that supports shell commands
# Required packages:
# pip install barcode
# pip install Pillow
import subprocess
import sys

try:
    import barcode
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-barcode"])

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

import barcode
from barcode.writer import ImageWriter
from PIL import Image

try:
    # Ask the user to input the number (12 digits)
    # Inputs of longer numbers (> 12 digits) will be cut after 12 digits (only first 12 digits are considered)
    number = input("Enter the code (12 digits) to generate the barcode : ")

    # Pad with leading zeros to make it 12 digits long, independent of user input
    number = number.zfill(12)

    # Generate the barcode
    barcode_format = barcode.get_barcode_class('upc')
    my_barcode = barcode_format(number, writer=ImageWriter())
    # Generated barcode will be saved in PNG format in the working directory, as well
    filename = my_barcode.save("generated_barcode")

    # Open and show the generated barcode image
    Image.open(f'{filename}').show()
    print("Barcode with number "+number+" was created.")
    print("\n")

except Exception as e:
    print(f"An error occurred: {e}")