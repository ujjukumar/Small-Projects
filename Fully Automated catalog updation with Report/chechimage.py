#!/usr/bin/env python3

import os
from PIL import Image

path = 'supplier-data/images/'

for item in os.listdir(path):
    f, e = os.path.splitext(item)
    file = os.path.join(path, item)
    if e == '.tiff':
        with Image.open(file) as im:
            f, e = os.path.splitext(file)
            outfile = f + '.jpeg'
            im.convert("RGB").resize((600, 400)).save(outfile)