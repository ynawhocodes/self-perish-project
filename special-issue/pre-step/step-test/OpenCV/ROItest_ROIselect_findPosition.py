# selectROI로 관심영역 지정 및 표시, 저장 (roi_select_img.py)

import cv2, numpy as np
import sys

img = cv2.imread('./img_05.jpg')

if img is None:
    print('Image load failed')
    sys.exit()

x,y,w,h	= cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]  
    print(x, y, w, h)

cv2.waitKey(0)
cv2.destroyAllWindows()