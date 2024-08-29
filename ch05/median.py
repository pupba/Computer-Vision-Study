import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
median = cv2.medianBlur(img,7)
cv2.imshow("median",median)
cv2.waitKey(0)
cv2.destroyAllWindows()