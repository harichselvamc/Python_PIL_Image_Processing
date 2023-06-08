from PIL import Image, ImageFilter

# load image
image = Image.open("dog.png")

# apply effect
newImage = image.filter(ImageFilter.EMBOSS)

# display image
newImage.show()

