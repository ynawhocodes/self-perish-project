import numpy
import cv2 
 
img = cv2.imread('img_01.jpg') 
 
verticalAppendedImg = numpy.vstack((img,img))

 
cv2.imshow('Vertical Appended', verticalAppendedImg)

 
cv2.waitKey(0)
cv2.destroyAllWindows()
