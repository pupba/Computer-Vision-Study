import cv2
import random

# 이미지 로드
image = cv2.imread('test.png')
if image is None:
    print("이미지를 로드할 수 없습니다.")
    exit()
sp = image.shape
image = cv2.resize(image,(int(sp[1]*0.5),int(sp[0]*0.5)),cv2.INTER_LANCZOS4)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.Canny(gray,50,200)
cv2.imshow("thres",thresh)
# 외곽선 찾기
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 외곽선 근사화
for contour in contours:
    # 허용 오차 설정
    epsilon = 0.02 * cv2.arcLength(contour, True)  # 주변 길이에 비례
    approx = cv2.approxPolyDP(contour, epsilon, True)
     # 랜덤 색상 생성
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # 근사화된 외곽선 그리기
    cv2.drawContours(image, [approx], -1, color, 2)

# 결과 이미지 출력
cv2.imshow('Approximated Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
