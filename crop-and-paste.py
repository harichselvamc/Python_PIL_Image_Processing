from PIL import Image

# load image
image = Image.open("cat.png")
dog = Image.open("dog.png")
image.show()

# crop
box = (100,188,547,591)
croppedImg = image.crop(box)
croppedImg.show()

# paste
image.paste(croppedImg, (447, 400))
image.paste(dog, (0, 0))
image.paste(croppedImg, (0, 400))
image.show()
