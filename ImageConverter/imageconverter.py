from PIL import Image
import numpy as np

#Save exported file as UTF8
import sys
sys.stdout = open(1, 'w', encoding='utf-8', closefd=False)

img = Image.open('image2.bmp').convert('L')

np_img = np.array(img)
np_img = ~np_img  # invert B&W
np_img[np_img > 0] = 1

pixels = np_img.tolist()
export_string = f"image = {pixels}"

with open('image.py', 'w', encoding='utf-8') as f:
    f.write(export_string)