import cv2
import numpy as np
from numba import jit
from copy import copy

def mse(imageA, imageB):
    # 두 이미지의 차이를 계산
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def psnr(imageA, imageB):
    # MSE 계산
    error = mse(imageA, imageB)
    if error == 0:
        return float('inf')  # 두 이미지가 동일할 경우 PSNR은 무한대
    MAX_PIXEL_VALUE = 255.0  # 8비트 이미지의 최대 픽셀 값
    return 10 * np.log10((MAX_PIXEL_VALUE ** 2) / error)

if __name__ == "__main__":
    im = cv2.imread("cat1.jpg")
    zim = copy(im) # 저화질 이미지
    zim = cv2.blur(zim,(5,5))
    cv2.imshow("k(5,5) img",zim)
    psnr_ori = psnr(im,zim)

    print(f"k(5,5) 유사도: {psnr_ori} dB")
    
    zim = cv2.blur(zim,(9,9))
    psnr_val = psnr(im,zim)
    
    print(f"k(9,9) 유사도 : {psnr_val} dB")

    cv2.imshow("img",im)
    cv2.imshow("k(9,9) img",zim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()