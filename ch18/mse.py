import cv2
import numpy as np
from numba import jit


@jit
def mse(imageA:np.ndarray, imageB:np.ndarray):
    # 두 이미지의 차이를 계산
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


if __name__ == "__main__":
    im1 = cv2.imread("cat1.jpg")
    im2 = cv2.imread("dog1.jpg")
    ratio = mse(im1,im2)
    print(f"유사도 : {ratio}")

    cv2.imshow("img1",im1)
    cv2.imshow("img2",im2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()