import cv2
import numpy as np
import random
# 이미지 로드
image = cv2.imread('test.png')
sp = image.shape
image = cv2.resize(image,(int(sp[1]*0.5),int(sp[0]*0.5)),cv2.INTER_LANCZOS4)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진화
_, thresh = cv2.threshold(gray, 162, 255, cv2.THRESH_BINARY)
cv2.imshow("thres",thresh)
# 윤곽선 찾기 (8-way connectivity)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선에 라벨 붙이기
for i, contour in enumerate(contours):
    # 윤곽선의 중심점 계산
    M = cv2.moments(contour)
    if M['m00'] != 0:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
    else:
        cX, cY = 0, 0

    # 랜덤 색상 생성
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # 윤곽선 그리기
    cv2.drawContours(image, contours, i, color, 2)

# 결과 이미지 출력
cv2.imshow('Labeled Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
