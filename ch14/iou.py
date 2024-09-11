import cv2
import numpy as np
def IoU(image:np.ndarray,mask:np.ndarray)->float:
    # 마스크를 이진형태로 변환
    _,bin_mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

    # Intersection과 Union
    intersection = np.logical_and(bin_mask,bin_mask).sum()
    union = np.logical_or(bin_mask,bin_mask).sum()
    # IoU
    iou = intersection / (union + 1e-6) # zero division을 방지하기 위해 작은 값 추가
    return iou

img = cv2.imread("cat.png")
h,w,_ = img.shape
img = cv2.resize(img,(int(w//2),int(h//2)),interpolation=cv2.INTER_LANCZOS4)
mask_im = cv2.imread("cat_mask.png")
mask_im = cv2.resize(mask_im,(int(w//2),int(h//2)),interpolation=cv2.INTER_LANCZOS4)
mask = cv2.cvtColor(mask_im,cv2.COLOR_BGR2GRAY)
mask[mask!=255] = 0
mask = ~mask


print(IoU(img,mask))

cv2.imshow("original",img)
cv2.imshow("mask_im",mask_im)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()