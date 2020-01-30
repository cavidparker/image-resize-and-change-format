
# you can change any .jpg/.png /.jpeg

from PIL import Image
import os, sys

path = "C:/Users/88016/Desktop/image resize/mobile_phone/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'JPEG', quality=90)

resize()