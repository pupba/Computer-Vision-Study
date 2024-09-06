import cv2
import numpy as np

image = cv2.imread("window.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 해리스 코너 검출
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# 결과 이미지를 복사하여 코너 표시
image[dst > 0.01 * dst.max()] = [0, 0, 255]  # 코너 부분을 빨간색으로 표시

cv2.imshow("Harris",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
