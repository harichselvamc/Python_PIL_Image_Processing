# Import module
from PIL import Image,ImageOps ,ImageDraw,ImageFont

# Load image from disk (change the path)
im = Image.open("cat.png")

# Show image
im.show()

# Save image as bitmap
im.save("cat.bmp")
