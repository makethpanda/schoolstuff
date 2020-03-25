# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:47:58 2020

@author: juju
"""


from PIL import Image
img = Image.open("pic.jpg")
#we open a specific image from our computer and set it as the img variable
img.show()
image_data = img.load()
#read the image data
height, width = img.size
#store the image size
for weee in range(height):
    for weeee in range(width):
        r,g,b = image_data[weee,weeee]
        #filter the green
        #image_data[weee,weeee] = r,0,b
        #switcheroo.exe ||| switches the coulours around 
        image_data[weee,weeee] = g,b,r


img.save("changed.jpeg")
#save as new image