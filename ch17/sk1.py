import cv2
import numpy as np

def skeletonize(img):
    """ OpenCV function to return a skeletonized version of img, a Mat object"""

    #  hat tip to http://felix.abecassis.me/2011/09/opencv-morphological-skeleton/

    img = img.copy() # don't clobber original
    skel = img.copy()

    skel[:,:] = 0
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

    while True:
        eroded = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
        temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)
        temp  = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img[:,:] = eroded[:,:]
        if cv2.countNonZero(img) == 0:
            break

    return skel


# 이미지 읽기
image = cv2.imread('h.png', cv2.IMREAD_GRAYSCALE)
h,w = image.shape
# resize
image = cv2.resize(image,(int(w//2),int(h//2)),interpolation=cv2.INTER_LANCZOS4)
# 스켈레토나이즈 수행
skeleton = skeletonize(image)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Skeleton', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()
