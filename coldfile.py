#importing some packages
import os
import math
import random as rand
import numpy as np
#import scipy

from PIL import Image

normal_temperature = 36.6
notnormal_temperature = 37
#file name and width
'''
    Important stuff below
'''

file = "heatpic.jpeg"
pixel_width = 1920
pixel_height = 1280


try:
    im = Image.open(file)

    rgb_im = im.convert('RGB')
    max_r,max_g,max_b = []
    for i in pixel_width:
        for j in pixel_height/2:
            r, g, b = rgb_im.getpixel((i, j))
            max_r.append(r)
            max_g.append(g)
            max_b.append(b)

    print(mar_r,max_g,max_b)

    morethan = 10

    for i in max_r:
        i=0
        if(max_r>200 and max_g<50 and max_b < 50):
            i++                               '''
        if(i>(morethan-1)):
            print("nor normal")
            break
                                            '''
except FileNotFoundError:
    print("not normal")
    
if(pixel_width < (1980/3*0.8)):
    print("Not normal")

        
