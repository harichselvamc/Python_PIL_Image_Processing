# Import PIL
from PIL import Image, ImageOps

# create image
im1 = Image.open("dog.png")

# flip vertically
im2 = ImageOps.flip(im1)

# show image
im2.show()

 
