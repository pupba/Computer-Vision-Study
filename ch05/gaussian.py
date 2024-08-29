import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
gaussian = cv2.GaussianBlur(img,(0,0),sigmaX=3) # sigmaX의 값에 따라 필터링 강도 바뀜 
cv2.imshow("gaussian",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()