import cv2
 
# 이미지 읽기
img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  
# 사각형 그리기
img = cv2.rectangle(img, (350, 25), (610, 230), (255, 0, 0), 3)
# 사각형을 그릴 이미지, 사각형의 좌측상단좌표, 우측하단좌표, 테두리 색, 테두리 두께
img = cv2.rectangle(img, (490, 180), (760, 360), (255, 0, 0), 3)
img = cv2.rectangle(img, (390, 380), (670, 530), (255, 0, 0), 3)
img = cv2.rectangle(img, (110, 180), (365, 480), (0, 255, 0), 3)
 
# 텍스트 넣기
cv2.putText(img, 'Coffee', (360, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
# 텍스트를 넣을 이미지, 텍스트 내용, 텍스트 시작 좌측하단좌표, 글자체, 글자크기, 글자색, 글자두께, cv2.LINE_AA(좀 더 예쁘게 해주기 위해)
cv2.putText(img, 'Coffee', (500, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Coffee', (400, 520), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Cake', (120, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA) 
 
 
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
