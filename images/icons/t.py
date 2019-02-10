#import PIL
from PIL import Image
sizes = [(128,128), (144,144), (152,152), (192,192), (256,256)]
image = 'icon.png'

for size in sizes:
    im = Image.open(image)
    im.thumbnail(size)
    im.save("icon-"+str(size[0]) + "x" +  str(size[1]) + ".png", "PNG")
