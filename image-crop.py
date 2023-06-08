from PIL import Image

# load image
image = Image.open("cat.png")
image.show()

# crop
box = (100,188,547,591)
croppedImg = image.crop(box)
croppedImg.show()

