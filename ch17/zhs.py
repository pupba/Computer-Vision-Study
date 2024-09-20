import numpy as np
import cv2
from numba import jit,prange

@jit
def thinning_iteration(im, iter):
    I, M = im.copy(), np.zeros(im.shape, np.uint8)
    for i in prange(1, im.shape[0] - 1):
        for j in prange(1, im.shape[1] - 1):
            p2 = I[i-1, j]
            p3 = I[i-1, j+1]
            p4 = I[i, j+1]
            p5 = I[i+1, j+1]
            p6 = I[i+1, j]
            p7 = I[i+1, j-1]
            p8 = I[i, j-1]
            p9 = I[i-1, j-1]

            A = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + \
                (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + \
                (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + \
                (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
            B = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
            m1 = p2 * p4 * p6 if iter == 0 else p2 * p4 * p8
            m2 = p4 * p6 * p8 if iter == 0 else p2 * p6 * p8

            if A == 1 and B >= 2 and B <= 6 and m1 == 0 and m2 == 0:
                M[i, j] = 1

    return I & ~M

def thinning(src):
    dst = src.copy() // 255
    prev = np.zeros(src.shape, np.uint8)
    diff = None

    while True:
        dst = thinning_iteration(dst, 0)
        dst = thinning_iteration(dst, 1)
        diff = np.abs(dst - prev)
        prev = dst.copy()
        if np.sum(diff) == 0:
            break

    return dst * 255

# 이미지 읽기
image = cv2.imread('h.png', cv2.IMREAD_GRAYSCALE)
h, w = image.shape
# resize
image = cv2.resize(image, (int(w // 2), int(h // 2)), interpolation=cv2.INTER_LANCZOS4)
# 이진화
_, bw2 = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
# Zhang-Suen 스켈레톤화 수행
bw2 = thinning(bw2)

# 결과 출력
cv2.imshow("original",image)
cv2.imshow('Skeleton', bw2)  # 스켈레톤을 0-255 범위로 변환
cv2.waitKey(0)
cv2.destroyAllWindows()
