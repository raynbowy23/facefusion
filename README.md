## About
This is a repo which I programmed for International collegiate Virtual Reality Contest 2019 (IVRC) in Tokyo, Japan. 
Please refer to this site (sorry for Japanese). 

This is our paper without peer review in Japanese (http://conference.vrsj.org/ac2019/program/common/doc/pdf/2B-04.pdf).

In this program, we are mixing dataset's and participants' faces with StyleGAN encoder https://github.com/Puzer/stylegan-encoder which latent features represent mixing face of two input images.

## Prerequisite

Python 3
cuda settings
`pip3 install -r requirements.txt`

## Explanation


Here explains each python files for data preprocessing.

`lighten_image.py` for emphasize light condition.

`find_face.py` for cropping image to adjust to its face.

`resize.py` for resizing face in image to adjust to input image.

`align_images.py` for aligning face image with haar cascade.

`encode_images.py` for generating unexist human image with PGGAN.

`mix.py` for mixing parents image (generated male/female face image and participants face image).

`combine.py` for combining these two images.

## Usage

You can actually upload images to and download from Google Drive. (In actual experiment, we showed to participants through Web monitor and this system is out of this repo.)

At first, download 'haarcascade_frontalface_alt2.xml' for detecting face image.

Then, you can run `bash reborn.sh` to make whole programs work. Please make sure the argments variables in shell file match to your environment.

