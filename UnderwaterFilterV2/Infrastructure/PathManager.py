import platform
import os
import sys

"""
Managing path for Mac, Linux and windows

2022.12.22  Originally created  Hyunjin Cho
"""

#Input file path
def ImageInputPathManager(Device,Extension):
    Directory = os.path.dirname(sys.argv[0])
    if(platform.system()=='Windows'):
        return '%s\\OriginalPhotos\\%s\\*.%s'%(Directory,Device,Extension)
    elif(platform.system()=='Darwin' or platform.system()=='Linux'):
        return '%s/OriginalPhotos/%s/*.%s'%(Directory,Device,Extension)
    else:
        raise Exception('Invalid Operating System')

#Output file path 
def ImageOutputPathManager(Device,Filter):
    Directory = os.path.dirname(sys.argv[0])
    if(platform.system()=='Windows'):
        return '%s\\ProcessedPhotos\\%s\\%s'%(Directory,Device,Filter)
    elif(platform.system()=='Darwin' or platform.system()=='Linux'):
        return '%s/ProcessedPhotos/%s/%s'%(Directory,Device,Filter)
    else:
        raise Exception('Invalid Operating System')

#Output folder path
def ImageOutputFolderPathManager(Device,Filter,ImageFile):
    Directory = os.path.dirname(sys.argv[0])
    if(platform.system()=='Windows'):
        return '%s\\ProcessedPhotos\\%s\\%s\\%s'%(Directory,Device,Filter,ImageFile)
    elif(platform.system()=='Darwin' or platform.system()=='Linux'):
        return '%s/ProcessedPhotos/%s/%s/%s'%(Directory,Device,Filter,ImageFile)
    else:
        raise Exception('Invalid Operating System')