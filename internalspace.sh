#!/bin/sh

CMDNAME=`basename $0`

if [ $# -ne 1 ]; then
    echo "Usage: $CMDNAME image_file" 1>&2
    exit 1
fi

IMAGE_NUMBER=$1

echo "${IMAGE_NUMBER}.jpg"
python align_images.py ${IMAGE_NUMBER}.jpg aligned_images/
python find_face.py --image_file ${IMAGE_NUMBER}.jpg
python resize.py ${IMAGE_NUMBER}.jpg
python encode_images.py --src_img ./sized_img/${IMAGE_NUMBER}.jpg
python mix.py ${IMAGE_NUMBER}