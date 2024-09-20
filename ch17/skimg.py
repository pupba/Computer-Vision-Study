import cv2
from skimage.morphology import skeletonize
import numpy as np
image = cv2.imread('h.png', cv2.IMREAD_GRAYSCALE)

ske = skeletonize(image)
skeleton_uint8 = (ske * 255).astype(np.uint8)

cv2.imshow("original",image)
cv2.imshow('Skeleton', skeleton_uint8)  # 스켈레톤을 0-255 범위로 변환
cv2.waitKey(0)
cv2.destroyAllWindows()