import numpy as np
import cv2

img = cv2.imread("test.png",cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
kernel = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
filtering = cv2.filter2D(img,-1,kernel=kernel)
filtering = np.uint8(filtering)

cv2.imshow("filter",filtering)
cv2.waitKey(0)
cv2.destroyAllWindows()