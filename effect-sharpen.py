from PIL import Image, ImageFilter

# load image
image = Image.open("cat.png")

# apply effect
newImage = image.filter(ImageFilter.SHARPEN)

# display image
newImage.show()

