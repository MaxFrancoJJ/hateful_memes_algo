from os import path
import pandas as pd
from PIL import Image
import numpy as np
import os
import glob
from IPython.display import clear_output

def image_to_df(dirPath=path.curdir + "/data/img/", size = (64,64)):


    """
        This functions takes in directory full of images and resizes them into same size by adding padding to each image
        its takes some time to run

        image_rize(dirPath, directory)

    dirPath == path.curdir + "/data/img/"
    directory == path.curdir+'/data/img_with_margins'

    """
    # Create empty  list
    my_list = []
    #list of files names to
    image_files = [name for name in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, name))]

    for i in range(0,len(image_files)):
        #import image
        img=Image.open(dirPath+image_files[i])
        #resize image
        resized_img = img.resize(size)
        #convert image to array
        arr_img = np.array(resized_img)
        #regularize pixel values & flatten
        flat_image = (arr_img/255).flatten()
        #convert image to list
        ready_img = flat_image.tolist()
        #append image to list
        my_list.append(ready_img)

        #progress check
        if (i+1) % 100 == 0:
            clear_output(wait=True)
            print(f'{i+1}/{len(image_files)} images processed')

    df = pd.DataFrame(my_list)

    df = df.fillna(0)

    #Add file names in to data set to be able to merge into NLP dataset
    df['img_name'] = image_files

    return df
