# selectROI로 관심영역 지정 및 표시, 저장 (roi_select_img.py)
import cv2, numpy as np
import sys

# mac test
# img = cv2.imread('/Users/yang/project/self-perish-project/special-issue/pre-step/step-test/OpenCV/img_05.jpg')

# window test - notebook
# img = cv2.imread('C:\\Users\\nw139\OneDrive\\바탕 화면\\images\\image_1.jpg')
img = cv2.imread('./image_1.jpg')
if img is None:
    print('Image load failed')
    sys.exit()

x,y,w,h	= cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]  
    print(x, y, w, h)

cv2.waitKey(0)
cv2.destroyAllWindows()