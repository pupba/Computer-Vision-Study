import cv2
from skimage.metrics import structural_similarity as ssim

# 이미지 읽기
imageA = cv2.imread('cat1.jpg')
cv2.imshow("im1",imageA)
imageB = cv2.imread('rabbit1.jpg')
# imageB = cv2.imread('dog1.jpg')
# imageB = cv2.imread('cat2.jpg')
cv2.imshow("im2",imageB)

# 이미지를 그레이스케일로 변환 (SSIM 계산을 위해)
imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# SSIM 계산
ssim_index, _ = ssim(imageA_gray, imageB_gray, full=True)

print(f'SSIM: {ssim_index}')

cv2.waitKey(0)
cv2.destroyAllWindows()