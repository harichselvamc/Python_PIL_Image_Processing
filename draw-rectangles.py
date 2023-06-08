from PIL import Image, ImageColor, ImageDraw
from random import randrange

# create image
image = Image.new("RGB", (512, 512), ImageColor.getrgb("#ffffff"))
draw = ImageDraw.Draw(image)

# draw lines at random positions
for n in range(0,30):
    x = randrange(512)
    y = randrange(512)
    w = randrange(100)
    h = randrange(100)
    c = [ "red","green","blue", "yellow", "orange", "purple" ]
    color = c[randrange(len(c))]

    # function .rectangle() draws a rectangle 
    draw.rectangle((x, y, x+w, y+h), fill=color, outline="black")

# display image
image.show()

 
