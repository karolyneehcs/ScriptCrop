from PIL import Image
import cv2
from cv2 import INTER_CUBIC
import numpy as np
import matplotlib.pyplot as plt
import os
import math 


source_folder = 'C:\\Users\\anaka\\Documents\\TCC\\StudioGhibli\\'
destination_folder = 'C:\\Users\\anaka\\Documents\\TCC\\StudioGhibli\\'
directory = os.listdir(source_folder)
frac = 0.5334

for item in directory:
    image = Image.open(source_folder + item)
    img = np.array(image).astype(np.float32)
    y,x,c = img.shape
    startx = math.floor(x-(((1-frac)/2)*x))
    starty = math.ceil(y-(((1-frac)/2)*y))
    imgResize = img[0:1024, math.ceil(((1-frac)/2)*x):startx]
    # cv2.imwrite(destination_folder + 'resized' + item[:-4] + '.jpg', imgResize)
    newImage = Image.fromarray(imgResize.astype(np.uint8))
    newImage.save("resized" + item[:-4] + ".jpg")
    print("resized" + item[:-4])