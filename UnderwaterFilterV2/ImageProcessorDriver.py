import cv2
import pathlib
import sys
import os
import numpy as np
from glob import glob
from Infrastructure.Enums import Device, Extension
from Infrastructure.PathManager import *
from Helpers.MessagePrompt import PromptInputMessage,PromptFilterInputMessage
from pathlib import Path
from Helpers.PromptColor import *
import ImageFilter.Filters as filters


"""
Unverwater image processor V2

2022.12.22  Originally created  Hyunjin Cho
"""

#Prompt user to ask which device
device = PromptInputMessage('Test pictures from device:',[dev for dev in dir(Device) if not dev.startswith('__')])
#Prompt user to ask which file extension
extension = PromptInputMessage('Test pictures with extension:',[ext for ext in dir(Extension) if not ext.startswith('__')])
#Prompt user to ask which filter
filterList = PromptFilterInputMessage('Filter images with filter:',[filter for filter in dir(filters) if not filter.startswith('__') and filter!='cv2'])

#store the actual data from the enum
Device = eval("Device."+device+".value")
Extension = eval("Extension."+extension+".value")

#Get the files with the device and extension information
img_mask = ImageInputPathManager(Device, Extension)
img_paths = glob(img_mask)



if len( img_paths)==0:
    raise Exception(StringInRed("No matching images"))
else:
    FilterName = "".join(filterList)
    for img_path in img_paths:
        #print which photo is being processed
        print('processing %s...' % img_path)
        image = cv2.imread(img_path,cv2.IMREAD_COLOR)
        for filter in filterList:
            image = eval('filters.%s(image)'%filter) 
            #if this exception is caught, it is likely that there is an error in the filter
            if(not isinstance(image,np.ndarray)):
                raise Exception(StringInRed('Check for error in the filter: %s'%filter))
       
        #get the path for the output image file
        pathlib.Path(ImageOutputPathManager(Device,FilterName)).mkdir(parents=True, exist_ok=True)
        #Write the image to the path
        cv2.imwrite(ImageOutputFolderPathManager(Device,FilterName,os.path.split(img_path)[1]), image)