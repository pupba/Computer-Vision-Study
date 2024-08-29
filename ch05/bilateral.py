import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
bilateral = cv2.bilateralFilter(img,d=-1,sigmaColor=10,sigmaSpace=5)
cv2.imshow("bilateral",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()