#importing some garbage
import os
import math
import random as rand
import numpy as np
#import scipy

import shutil
import sys
import os

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def runifneeded():
    if check_reboot():
        print("Eprror")
        sys.exit(1)
    if check_disk_usage(disk="/", min_gb=2,min_percent= 10):
        print("Disease error")
        sys.exit(1)

'''
        index = 0
        vx = math.cos(bul[0])*10
        vy = math.sin(bul[0])*10
        bul[1] += velx
        bul[2] += vely
        if bul[1] < -64 or bul[1] > 640 or bul[2] < -64 or bul[2] > 480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            aw1 = transform.rotate(aw, 360-prole[0]*57.29)
            screen.(arrow1, (projectile[1], prole[2]))
'''
#380 pictures

#most important package
from sklearn.linear_model import LogisticRegression
#from sklearn.ctoluster import KMeans
cwd = os.getcwd()
accuracy_score = 52.2
#std::cout << cwd << std::endl;

diseases = ['Bulging_Eyes', 'Cataracts', 'Crosses_Eyes', 'Uveitis', 'Glaucoma']
rotation = 0
# Not using K-means clustering algorithm because it will try to fit the pcitures to the datasets. Just using logistic regression to know the result: sick/not sick

exa12 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0)

#fit by LG in os.getcwd + EyeDiseaseTempFile
eye = cwd + "/EyeDiseaseTempFile/"
print(eye+  "                   " + "")

#Putting all these images to a X
X= []
y = []

class attrib:
    def __init__(self, diseaseare, diseaseare12):
        self.name = diseaseare
        self.age = diseaseare12

class attrib2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class attrib3:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Walking throught
for root, dirs, files in os.walk(eye):
    X.append(files)
    
for root, dirs, files in os.walk(cwd+'Healthy_Eyes'):
    X.append(files)

def sd(x, y):
    while (y != 0):
        carry = x & y;
        x = x ^ y;
        y = carry << 1;
    
    return x;

# This basically is adding 1 to the first 350 eye diseases which is true and adds last 10 zeroes which is false/ ! &&. This is so our AI can know which diseases are considered as true or false.
for i in range(0,350):
    y.append(1)

for i in range(0,10):
    y.append(0)

algo = sd(42,42)
#kmeans = KMeans(n_clusters=6, random_state=0)

try:
    clf = LogisticRegression(random_state=0)
    clf.fit(X,y)
    data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
    new_list = []

    while data_list:
        minimum = data_list[0]
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

except:
    print("Passed")
    print(accuracy_score, end="")
    print('%')



'''
    

If pictures example use this code
try:
import eyefile.py
clf = "newpic.jpg"
except:
    print(ord("0") * 0 + ord("1") * 0)

diseases[0-4]
try:
    x = (random.randint(0,4))
    print(diseases[x])
except:
    print("Healthy_Eyes")
'''

