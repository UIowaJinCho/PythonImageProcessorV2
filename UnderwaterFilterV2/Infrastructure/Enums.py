from aenum import Enum

"""
Enums for the device of the images, and file extensions

2022.12.22  Originally created  Hyunjin Cho
"""

#Folder names in OriginalPhotos, ProcessedPhotos
class Device(Enum):
    GOPRO = 'Gopro'
    DIVEROID = 'Diveroid'

#Extensions, code for MP4(video) is not in this verseion
class Extension(Enum):
    #MP4 = 'MP4'
    JPEG = 'jpeg'
    JPG = 'jpg'