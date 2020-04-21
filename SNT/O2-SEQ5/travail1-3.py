# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:43:59 2020

@author: Julien
"""


from PIL import Image
img = Image.new("RGB",(160,80),(0,0,255))
for x in range (40):
    img.putpixel((x,10),(255,0,0))
for y in range (80):
    img.putpixel((80,y),(0,255,0))
    
img.show()
