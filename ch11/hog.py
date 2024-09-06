import cv2

# HOG 분류기 초기화
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 이미지 불러오기
image = cv2.imread('people.jpg')

# 보행자 검출
boxes, weights = hog.detectMultiScale(image, winStride=(8, 8), padding=(8, 8), scale=1.05)

# 검출된 보행자에 사각형 그리기
for (x, y, w, h) in boxes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 결과 이미지 표시
cv2.imshow('Detected Pedestrians', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
