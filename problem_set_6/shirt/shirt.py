import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_image = sys.argv[1]
input_image_name, in_extension = os.path.splitext(input_image)

output_image = sys.argv[2]
output_image_name, out_extension = os.path.splitext(output_image)

if in_extension.lower() not in ['.jpg', '.png', '.jpeg']:
    sys.exit("Invalid input")

if out_extension.lower() not in ['.jpg', '.png', '.jpeg']:
    sys.exit("Invalid output")

if out_extension.lower() != in_extension.lower():
    sys.exit("Input and output have different extensions")

try:
    with Image.open(input_image) as im1:
        shirt = Image.open('shirt.png')
        shirt_size = shirt.size

        resized_input = ImageOps.fit(im1, shirt_size)
        resized_input.paste(shirt, (0, 0), shirt)
        resized_input.save(output_image)
except FileNotFoundError:
    sys.exit("Input does not exist")


