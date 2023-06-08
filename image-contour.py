from PIL import Image, ImageFilter

# load image
image = Image.open("/home/cat/cat3.png")

# apply effect using contour kernel
newImage = image.filter(ImageFilter.CONTOUR)

# display image
newImage.show()

