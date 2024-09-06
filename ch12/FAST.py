import cv2
import numpy as np

image = cv2.imread("window.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# FAST 코너 검출기 초기화
fast = cv2.FastFeatureDetector_create()

# 코너 검출
keypoints = fast.detect(gray, None)

# 검출된 키포인트를 이미지에 표시
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("FAST",image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
