import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("test.png",cv2.IMREAD_COLOR)
    img = cv2.resize(img,(512,600),interpolation=cv2.INTER_LANCZOS4)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("Origin",img)

    # 빨간색 범위 설정 (HSV)
    lower_red = np.array([0, 100, 100])  # 하한값
    upper_red = np.array([10, 255, 255])  # 상한값

    mask = cv2.inRange(img_hsv, lower_red, upper_red)

    cv2.imshow("Red Masking",cv2.bitwise_and(img,img,mask=mask))

    cv2.waitKey(0)
    cv2.destroyAllWindows()