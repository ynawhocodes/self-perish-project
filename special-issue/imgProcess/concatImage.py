import numpy
import cv2 
 
img = cv2.imread('img_01.jpg') 
 
verticalAppendedImg = numpy.vstack((img,img))
horizontalAppendedImg = numpy.hstack((img,img,img))
 
cv2.imshow('Vertical Appended', verticalAppendedImg)
cv2.imshow('Horizontal Appended', horizontalAppendedImg)
 
cv2.waitKey(0)
cv2.destroyAllWindows()