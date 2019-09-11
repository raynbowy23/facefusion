import glob
import os
import sys


def get_last_file():
    DOWNLOADS_DIR = './img'
    FILE_BASE_NAME = 'raw'
    FILE_EXT = '.jpg'

    fileList = []
    # files = glob.glob(DOWNLOADS_DIR + FILE_BASE_NAME + '*' + FILE_EXT)
    files = glob.glob(os.path.join(DOWNLOADS_DIR, '*.jpg'))

    for file in files:
        # print(file)
        if file == (os.path.join(DOWNLOADS_DIR, FILE_BASE_NAME) + FILE_EXT):
            fileID = 0
        else:
            # print(os.path.join(DOWNLOADS_DIR, FILE_BASE_NAME) + ' (')
            file2 = file.replace(os.path.join(DOWNLOADS_DIR, FILE_BASE_NAME) + ' (', '')
            # print(file)
            fileID = file2.replace(')' + FILE_EXT, '')
            # print(fileID)
            fileID = int(fileID)
        element = {'id': fileID, 'path': file}
        fileList.append(element)
    sortedFileList = sorted(fileList, key = lambda x: x['id'])
    path = sortedFileList[-1]['path']
    # print(os.path.splitext(sortedFileList[-1]['path'])[0]) # return before .jpg
    new_path = path.replace(DOWNLOADS_DIR + '\\', '') #.replace(' (', '').replace(')', '')
    return new_path

print(get_last_file())