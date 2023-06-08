from PIL import Image, ImageColor, ImageDraw
from random import randrange

# create image
image = Image.new("RGB", (512, 512), ImageColor.getrgb("#ffffff"))
draw = ImageDraw.Draw(image)

# draw lines at random positions
for n in range(0,30):
    x = randrange(512)
    y = randrange(512)
    w = randrange(10)

    # function .line() draws a line 
    draw.line([(x,y), (x+100,y+100)], fill=(randrange(255), randrange(255), randrange(255)), width=w)

# display image
image.show()

 
