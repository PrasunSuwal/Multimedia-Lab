from PIL import Image
import os

# Absolute path to the images
jpg_path = 'prasun/LAB_03/lenna.jpg'

img = Image.open(jpg_path)

img.save('lenna.png', 'png')
img.save('lenna.tiff', 'TIFF')

jpg_size = os.path.getsize(jpg_path)
png_size = os.path.getsize('lenna.png')
tiff_size = os.path.getsize('lenna.tiff')

print("JPG size: {} bytes".format(jpg_size))
print("PNG size: {} bytes".format(png_size))
print("TIF size: {} bytes".format(tiff_size))

with open(jpg_path, 'rb') as f:
    data = f.read()
jpg_actual_size = len(data)
print("Actual JPG size: {} bytes".format(jpg_actual_size))
