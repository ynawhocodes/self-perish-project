# selectROI로 관심영역 지정 및 표시, 저장 (roi_select_img.py)
import cv2, numpy as np
import sys

# mac test
# img = cv2.imread('/Users/yang/project/self-perish-project/special-issue/pre-step/step-test/OpenCV/img_05.jpg')

# window test - notebook

# 절대 경로
img = cv2.imread('C:\\Users\\nw139\\image_1.jpg')

# 상대 경로로 했을 경우 해당 폴더로 이동 후 실행해야 ok
# img = cv2.imread('./image_1.jpg')

if img is None:
    print('Image load failed')
    sys.exit()

x,y,w,h	= cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]  
    print(x, y, w, h)

cv2.waitKey(0)
cv2.destroyAllWindows()