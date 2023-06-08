# Import PIL
from PIL import Image, ImageOps

# create image
im1 = Image.open("dog.png")

# invert image
im2 = ImageOps.invert(im1)

# show image
im2.show()

 
