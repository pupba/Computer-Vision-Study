import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
blur = cv2.blur(img,(3,3))
cv2.imshow("blur",blur)
mask = np.asarray([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]], dtype = np.float32)
sharpening_img = cv2.filter2D(blur,-1, mask)
cv2.imshow("sharp",sharpening_img)
cv2.waitKey(0)
cv2.destroyAllWindows()