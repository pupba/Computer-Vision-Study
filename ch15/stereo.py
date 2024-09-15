import numpy as np
import cv2
from matplotlib import pyplot as plt

img_left = cv2.imread("./img_left.jpg",cv2.IMREAD_GRAYSCALE)

img_right = cv2.imread("./img_right.jpg",cv2.IMREAD_GRAYSCALE)


# 스테레오 매칭 객체 생성
# numDisparities : 깊이 맵을 계산할 때 사용할 최대 시차 값을 지정, 값은 16의 배수 
# blockSize : 매칭을 오ㅟ해 사용할 블록의 크기, 이 값은 홀수여야 하며, 일반적으로 5,7,9,11 등임
stereo = cv2.StereoBM.create(numDisparities=16,blockSize=9)

# 깊이 맵 계산
disparity_map = stereo.compute(img_left, img_right)

# 서브플롯 생성
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# 원본 이미지 (왼쪽)
axs[0].imshow(img_left, cmap='gray')
axs[0].set_title("Left Image")
axs[0].axis("off")

# 원본 이미지 (오른쪽)
axs[1].imshow(img_right, cmap='gray')
axs[1].set_title("Right Image")
axs[1].axis("off")

# 깊이 맵
axs[2].imshow(disparity_map, cmap='gray')
axs[2].set_title("Depth Map")
axs[2].axis("off")

# 결과 출력
plt.tight_layout()
plt.show()