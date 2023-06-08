# Import module
from PIL import Image

# Load image from disk
im = Image.open("cat.png")

# Resize image
im = im.resize(100,100)

# Show image
im.show()
