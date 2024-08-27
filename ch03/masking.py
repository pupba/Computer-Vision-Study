import cv2
import numpy as np

img = cv2.imread("test.png")
img = cv2.resize(img,(512,512),interpolation=cv2.INTER_LANCZOS4)

mask = np.zeros(img.shape[:2],dtype=np.uint8)
cv2.rectangle(mask,(100,100),(300,400),255,thickness=cv2.FILLED)
# 마스킹
# inv_mask = cv2.bitwise_and(img,img,mask=mask)
# inv_mask = cv2.bitwise_not(img,img,mask=mask)
# inv_mask = cv2.bitwise_or(img,img,mask=mask)
inv_mask = cv2.bitwise_xor(img,img,mask=mask)
cv2.imshow("inv_mask",inv_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()