import cv2

"""
The image filter logic code is located here.

2022.12.22  Originally created  Hyunjin Cho
"""

#If you add your filter in the following syntax it will automatically show up in the command prompt
def Filter1(image):
    b,g,r = cv2.split(image)
    b = cv2.subtract(b,20)
    g = cv2.subtract(g,80)
    r = cv2.add(r,30)
    return cv2.merge((b,g,r))

def FilterEdgeDetectionX(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    return sobelx

def FilterEdgeDetectionY(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    return cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

def FilterEdgeDetectionXY(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    return cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
