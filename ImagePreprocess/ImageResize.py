from os import path
import pandas as pd
from PIL import Image
import numpy as np
import os
import glob
from IPython.display import clear_output


def image_resize(dirPath=path.curdir + "/data/img/", directory=path.curdir+'/data/img_with_margins'):


    """
        This functions takes in directory full of images and resizes them into same size by adding padding to each image
        its takes some time to run

        image_rize(dirPath, directory)

    dirPath == path.curdir + "/data/img/"
    directory == path.curdir+'/data/img_with_margins'

    """
    #list of files names to
    image_files = [name for name in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, name))]
    # Number of images m
    m = len(image_files)

    # Define image size
    largestImage = {'width':0 , 'height': 0}
    for i in glob.glob(dirPath+'*', recursive=True):
        width, height = Image.open(i).size
        if width > largestImage['width']:
            largestImage['width'] = width + 10
        if height > largestImage['height']:
            largestImage['height'] = height + 10



    #create folder to store images with margins
    if os.path.isdir(directory):
        print('Folder already exists')
    else:
        os.mkdir(directory)

        for i in range(0,m):
            #create background image to use as padding so that all images are the same size
            padImage = Image.new('RGB',(largestImage['width'], largestImage['height']), (128, 0, 64))
            #import image
            img=Image.open(dirPath+image_files[i])
            #add padding to image
            padImage.paste(img, (10,10))
            #save images to folder
            padImage.save(directory+f'/{image_files[i][0:5]}_margin.png')
            if (i+1) % 10 == 0:
                clear_output(wait=True)
                print(f'{i+1}/{m} images processed')
