import cv2
import argparse

# 基本的なモデルパラメータ
FLAGS = None

# 学習済モデルの種類
cascade = ["default","alt","alt2","tree","profile","nose"]

# 直接実行されている場合に通る(importされて実行時は通らない)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cascade",
        type=str,
        default="default",
        choices=cascade,
        help="cascade file."
  )
    parser.add_argument(
        "--image_file",
        type=str,
        default="cut_source0.jpg",
        help="image file."
  )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.3,
        help="scaleFactor value of detectMultiScale."
  )
    parser.add_argument(
        "--neighbors",
        type=int,
        default=2,
        help="minNeighbors value of detectMultiScale."
  )
    parser.add_argument(
        "--min",
        type=int,
        default=30,
        help="minSize value of detectMultiScale."
  )

# パラメータ取得と実行
FLAGS, unparsed = parser.parse_known_args()        

# 分類器ディレクトリ(以下から取得)
# https://github.com/opencv/opencv/blob/master/data/haarcascades/
# https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/

if   FLAGS.cascade == cascade[0]:#"default":
    cascade_path = "./models/haarcascade_frontalface_default.xml"
elif FLAGS.cascade == cascade[1]:#"alt":
    cascade_path = "./models/haarcascade_frontalface_alt.xml"
elif FLAGS.cascade == cascade[2]:#"alt2":
    cascade_path = "./models/haarcascade_frontalface_alt2.xml"
elif FLAGS.cascade == cascade[3]:#"tree":
    cascade_path = "./models/haarcascade_frontalface_alt_tree.xml"
elif FLAGS.cascade == cascade[4]:#"profile":
    cascade_path = "./models/haarcascade_profileface.xml"
elif FLAGS.cascade == cascade[5]:#"nose":
    cascade_path = "./models/haarcascade_mcs_nose.xml"

cascade_path = "haarcascade_frontalface_default.xml"

# 使用ファイルと入出力ディレクトリ
image_path  = "./img/"  + FLAGS.image_file
output_path = "./sized_img/"

# ディレクトリ確認用(うまく行かなかった時用)
import os
# print(os.path.exists(image_path))
# print(os.path.exists(cascade_path))

#ファイル読み込み
image = cv2.imread(image_path)

#グレースケール変換
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image_gray)
#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)    
print(cascade)

#物体認識（顔認識）の実行
#image - CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
#objects - 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
#scaleFactor - 各画像スケールにおける縮小量を表します
#minNeighbors - 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
#flags - このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
#minSize - 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
facerect = cascade.detectMultiScale(image_gray, scaleFactor=FLAGS.scale, minNeighbors=FLAGS.neighbors, minSize=(FLAGS.min, FLAGS.min))

# print(facerect)

color = (255, 255, 255) #白

#顔部分を切り取る
for x,y,w,h in facerect:
    faced_image = image[0:y+h+(int)(y/2), x-(int)(x/2):x+w+(int)(x/2)]
    # faced_image = image[y:y+h, x:x+w]
    print(y)
    print(y-h-h)
    print(y+h+h)

# 検出した場合
if len(facerect) > 0:

    #検出した顔を囲む矩形の作成
    # for rect in facerect:
        # cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
        # cv2.imwrite(output_path, image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]])

    #認識結果の保存
    cv2.imwrite(os.path.join(output_path, FLAGS.image_file), faced_image)

else:
    print("Could not find any face")