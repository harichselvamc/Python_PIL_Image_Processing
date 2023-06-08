# Import PIL
from PIL import Image, ImageOps

# create image
im1 = Image.open("dog.png")

# turn image into gray scale
im2 = ImageOps.grayscale(im1)

# show image
im2.show()

 
