import cv2

image = cv2.imread("human.jpg")
image = cv2.resize(image,(int(image.shape[1]//2),int(image.shape[0]//2)),interpolation=cv2.INTER_LANCZOS4)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 분류기 로드
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# 눈 검출
eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(60,60))

# 바운딩 박스
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Cascade Classifier",image)
cv2.waitKey(0)
cv2.destroyAllWindows()