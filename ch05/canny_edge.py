import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
# cv2.Canny(이미지,하위 임계값,상위 임계값, sobal 마스크 크기)
edge = cv2.Canny(img,100,255)
cv2.imshow("canny",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()