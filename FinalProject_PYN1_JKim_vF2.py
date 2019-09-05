#!/usr/bin/env python
# coding: utf-8

# In[103]:


"""

Name:          Joshua Kim
Class:         Python Programming 1 - Summer 2019
Instructor:    Stefan Wojciechowski
Project:       Converting Web Scraped Images into ASCII Art
Modules used:  PIL > Image (tutorial: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)

"""

import os
from PIL import Image

gscale = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
pixel_cap = 255

# program to read in the image and define w x h ratio (height is fixed to 220 here, width varies depending on ratio)
def get_picture_matrix(pic, height):
    pic.thumbnail((height, 220))
    pixels = list(pic.getdata()) # getdata retrieves the pixel values of an image
    return [pixels[i:i + pic.width] for i in range(0, len(pixels), pic.width)] # copied/modified from PIL tutorial
    print(pixels)

# create an array to read every pixel in the image
# pixels in .jpegs are stored as 3-item tuples, e.g., (255, 255, 255), representing the RGB values
# it then converts the RGB tuple into a single float value
def get_color_matrix(pixels_matrix, algorithm_name = "luminosity"):
    color_matrix = []
    for row in pixels_matrix:
        color_row = []
        for p in row:
            if algorithm_name == "luminosity":
                luminosity = 0.21*p[0] + 0.72*p[1] + 0.07*p[2]
                # there are multiple ways to convert the RGB tuples into a single luminosity value, like a normal average
                # but i went with weighted averages suggested online (takes into account human perceptions of the RGB colors)
            else:
                raise Exception("Unrecognixed algo_name: %s" % algorithm_name)
            color_row.append(luminosity)
        color_matrix.append(color_row)
    return color_matrix
    print(color_matrix)

# normalize the float value againt a pre-set pixel-cap value
# this standardizes the values within a fixed range
def normalize_color_matrix(color_matrix):
    normalized_color_matrix = []
    max_pixel = max(map(max, color_matrix))
    min_pixel = min(map(min, color_matrix))
    for row in color_matrix:
        rescaled_row = []
        for p in row:
            r = pixel_cap * (p - min_pixel) / float(max_pixel - min_pixel)
            rescaled_row.append(r)
        normalized_color_matrix.append(rescaled_row)
    return normalized_color_matrix

# then finally convert the luminosity value into the proportionate ascii character based on the gray scale (gscale)
def convert_to_ascii(color_matrix, gscale):
    ascii_matrix = []
    for row in color_matrix:
        ascii_row = []
        for p in row:
            ascii_row.append(gscale[int(p/pixel_cap * len(gscale)) - 1])
        ascii_matrix.append(ascii_row)
    return ascii_matrix

# filepath = r"/Users⁩/joshuakim/python1_final_project⁩"
# subprocess.run(["pineapple_img.jpg", "-w", "2"])


"""
INPUT IMAGE FILE BELOW HERE
"""
pic = Image.open("seven_lions_img.jpg")

pixels = get_picture_matrix(pic, 200)

color_matrix = get_color_matrix(pixels, "luminosity")

re_color_matrix = normalize_color_matrix(color_matrix)

# big shout out to stefan!
ascii_matrix = convert_to_ascii(re_color_matrix, gscale)
for x in ascii_matrix:
    print("".join(x))


# In[101]:


print)mantis_shrimp_img.jpg)


# In[ ]:




