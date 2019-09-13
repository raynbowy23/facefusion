#coding: utf-8

import cv2
import numpy as np
import os
import sys
from PIL import Image

# python resize.py "number".jpg

def resize_image(original_img):

    # original_img = sys.argv[1]
    img_dir = './face_img'
    # img_dir = './lighten_imgs'
    save_dir = './sized_img'

    original_dir = os.path.join(img_dir, original_img)
    # print(original_dir)
    img = cv2.imread(original_dir, cv2.IMREAD_COLOR)

    orgHeight, orgWidth = img.shape[:2]
    size = (256,256)
    newImg = cv2.resize(img, size)

    # print(newImg.shape[:2])
    
    cv2.imwrite(os.path.join(save_dir, original_img), newImg)
    # cv2.imwrite('./img/1.jpg', newImg)

if __name__ == '__main__':
    resize_image(sys.argv[1])

    print("Done image resized")