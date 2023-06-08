# Import module
from PIL import Image

# Load image
im = Image.open("cat.png")

# Rotate image by degrees
im = im.rotate(45)

# Show image
im.show()
