import numpy as np
import cv2

img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))
cv2.imshow("origin",img)
for i in [3,6,10]:
    kernel = np.ones((i,i),np.uint8) / i ** 2
    filtering = cv2.filter2D(img,-1,kernel=kernel)
    cv2.imshow(f"{i}x{i}filter",filtering)
cv2.waitKey(0)
cv2.destroyAllWindows()