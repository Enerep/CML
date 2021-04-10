#Import packages
import os
import math
from shutil import copyfile
import shutil

tdir = "EyeDiseaseTempFile"

try:
    os.mkdir(tdir)
except OSError as error:
    print(error)

#Walking throught the directories and files

for root, dirs, files in os.walk("."):
    #Magic
    for file in files:
        fname, ftype = os.path.splitext(file)

        if ftype== ".jpeg":
            newPath = shutil.copy(root+'/'+file, tdir)


#Later
#os.rmdir(tdir)
