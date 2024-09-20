import cv2
import thinning
from copy import copy
img = cv2.imread("h.png",cv2.IMREAD_GRAYSCALE)
img_ = copy(img)
thinned = thinning.guo_hall_thinning(img_)
cv2.imshow("original",img)
cv2.imshow("guohall",thinned)

cv2.waitKey(0)
cv2.destroyAllWindows()