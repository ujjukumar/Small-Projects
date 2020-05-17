import os
import sys
from PIL import Image


path = 'images/'
for name in os.listdir(path):
    file = os.path.join(path, name)
    if os.path.isfile(file) and file != 'images/.DS_Store':
        with Image.open(file) as im:
            outfile = '/opt/icons/' + name + '.jpg'
            im.convert("RGB").rotate(90).resize((128, 128)).save(outfile)