import cv2
import numpy as np
import sys
import os

IMG_NAME = sys.argv[1]
im1 = cv2.imread(os.path.join('./father_imgs', IMG_NAME), cv2.IMREAD_COLOR)
im2 = cv2.imread(os.path.join('./mother_imgs', IMG_NAME), cv2.IMREAD_COLOR)

comb_img = cv2.hconcat([im1, im2])
cv2.imwrite(os.path.join('results', IMG_NAME), comb_img)