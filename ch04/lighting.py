import numpy as np
import cv2

white = np.ones(shape=(480,480),dtype=np.uint8) * 255
cv2.imshow("white",white)
black = np.zeros(shape=(480,480),dtype=np.uint8)
cv2.imshow("black",black)

cv2.waitKey(0)
cv2.destroyAllWindows()