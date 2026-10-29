# install Pillow instead of PIL!
from PIL import Image, ImageDraw

# create a new image, size is 500 pixels by 300 pixels (horizontal/vertical)
# for colors, search for color picker in Google to use the built-in -tool
img = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(img)



# for coordinates, see:
# https://www.plus2net.com/python/images/pil-text-anchor.jpg
# in ellipse on similar shapes we have two sets of coordinates
# e.g. here 100, 100 and 200, 200
# xy = 100, 100 is the starting point
# and 200, 200 is the bottom right
# means the ellipse size is 100 x 100 (200 - 100 = 100)
draw.ellipse((100, 100, 200, 200), fill=(100, 200, 100), outline=(0,0,0))

# finally, save the image to a file
img.save("pillow_test.png")