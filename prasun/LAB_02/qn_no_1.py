# Python program to view a BMP file using matplotlib

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def view_bmp_file(file_path):
    try:
        # Read the BMP file
        img = mpimg.imread(file_path)

        # Display the BMP file
        imgplot = plt.imshow(img)
        plt.show()

    except IOError:
        print("Unable to load image")

# Specify the path to the BMP file
file_path = "Images/image.bmp"

# Call the function to view the BMP file
view_bmp_file(file_path)