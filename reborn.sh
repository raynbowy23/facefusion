#!/bin/sh

SECONDS=0

time=$SECONDS

CMDNAME=`basename $0`

# if [ $# -ne 1 ]; then
#     echo "Usage: $CMDNAME image_file" 1>&2
#     exit 1
# fi

# IMAGE_NUMBER=$1
IMAGE_JPEG=`python latest_file.py`
# IMAGE_JPEG=${IMAGE_NUMBER}.jpg
# IMAGE_PNG=${IMAGE_NUMBER}.png

# echo "${IMAGE_NUMBER}.jpg"
echo ${IMAGE_JPEG}
# python image_downloader.py ${IMAGE_NUM}

# python align_images.py ${IMAGE_PNG}

python lighten_image.py "${IMAGE_JPEG}"
python find_face.py --image_file "${IMAGE_JPEG}"
python resize.py "${IMAGE_JPEG}"
python align_images.py "${IMAGE_JPEG}"
python encode_images.py --src_img ./sized_img/"${IMAGE_JPEG}"
python mix.py "${IMAGE_JPEG}"
python combine.py "${IMAGE_JPEG}"

python image_uploader.py "${IMAGE_JPEG}"

echo $time