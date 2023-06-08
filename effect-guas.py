from PIL import Image, ImageFilter

# load image
image = Image.open("/home/cat/cat3.png")

# apply effect
blurImage = image.filter(ImageFilter.GaussianBlur(3))

# display image
blurImage.show()

