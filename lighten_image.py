# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
import os

IMG_DIR = 'img'
IMG_FILE = sys.argv[1]
SAVE_DIR = 'lighten_imgs'

# 画像の読込(numpy.ndarrayで読み込まれる)
# image = cv2.imread('img/raw (10).jpg')
image = cv2.imread(os.path.join(IMG_DIR, IMG_FILE))

## γ値の定義(1より小さいと暗く、1より大きいと明るくなる)
gamma = 1.1

# ルックアップテーブルの生成
look_up_table = np.zeros((256,1), dtype=np.uint8)
for i in range(256):
    look_up_table[i][0] = 255* (float(i)/255) ** (1.0 / gamma)

# γ変換後の画像取得
image_gamma = cv2.LUT(image, look_up_table)

# シャープの度合い
# k = 2.0
# # # シャープ化するためのオペレータ
# sharp_operator = np.array([[0,        -k, 0],
#                 [-k, 1 + 4 * k, -k],
#                 [0,         -k, 0]])

# # # 作成したオペレータを基にシャープ化
# img_tmp = cv2.filter2D(image_gamma, -1, sharp_operator)
# img_sharp = cv2.convertScaleAbs(img_tmp)

# cv2.imwrite(os.path.join(SAVE_DIR, IMG_FILE), img_sharp)
cv2.imwrite(os.path.join(SAVE_DIR, IMG_FILE), image_gamma)
