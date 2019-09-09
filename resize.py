#coding: utf-8

import cv2
import numpy as np
import os
import sys

# def resize_image(sys.argv):

original_img = sys.argv[1]
img_dir = './sized_img'

original_img = os.path.join(img_dir, original_img)
print(original_img)
img = cv2.imread(original_img, cv2.IMREAD_COLOR)

orgHeight, orgWidth = img.shape[:2]
size = (256,256)
newImg = cv2.resize(img, size)

print(newImg.shape[:2])

cv2.imwrite('./img/1.jpg', newImg)