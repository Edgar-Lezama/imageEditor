#python.exe -m pip install --upgrade pip
#Install Pillow library to automate the image editing process
from PIL import Image, ImageEnhance, ImageFilter
import os

#path = ('Directory_Location')  Set custom directory paths
#pathOut = ('Directory_Location')  Set custom directory paths

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
