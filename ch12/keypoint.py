import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread("window.jpg")

# ORB 객체 생성
orb = cv2.ORB_create()

# 키 포인트 및 설명자 검출
keypoints, descriptors = orb.detectAndCompute(image, None)

# 키 포인트를 이미지에 그리기
image_with_keypoints = image.copy()

# 랜덤 색상으로 키 포인트 그리기
for kp in keypoints:
    # 랜덤 색상 생성 (BGR 형식)
    random_color = np.random.randint(0, 256, size=3).tolist()
    # 키 포인트 위치와 크기에 따라 원 그리기
    cv2.circle(image_with_keypoints, (int(kp.pt[0]), int(kp.pt[1])), int(kp.size / 2), random_color, 1)

# 결과 이미지 표시
cv2.imshow('Keypoints with Random Colors', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()