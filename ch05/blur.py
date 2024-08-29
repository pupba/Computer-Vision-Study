import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
blur = cv2.blur(img,(3,3))
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()