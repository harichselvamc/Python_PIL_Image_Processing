# Import PIL
from PIL import Image, ImageOps

# create image
im1 = Image.open("dog.png")

# flip horizontally
im2 = ImageOps.mirror(im1)

# show image
im2.show()

 
