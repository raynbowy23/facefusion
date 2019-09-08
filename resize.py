#coding: utf-8

import cv2
import numpy as np

img = cv2.imread('./img/yume.jpg', cv2.IMREAD_COLOR)

orgHeight, orgWidth = img.shape[:2]
size = (256,256)
newImg = cv2.resize(img, size)

print(newImg.shape[:2])

cv2.imwrite('./img/1.jpg', newImg)