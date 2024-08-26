import cv2
import numpy as np
img1 = cv2.imread("color.jpg")
img2 = cv2.imread("gray.jpg")

# 이미지 크기 확인
height,width,channel = img1.shape
print(f"세로 : {height}, 가로 : {width}, 채널(RGB,GRAY,RGBA) : {channel}")
# 반전
# cv2.imshow("origin",img1)
# cv2.imshow("reversed origin",~img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 크기 변경
re_img = cv2.resize(img1,(512,512),interpolation=cv2.INTER_LANCZOS4)
# interpilation 인자 종류
# cv2.INTER_NEAREST - 최근방 이웃 보간법
# cv2.INTER_LINEAR - 양선형 보간법(2x2 이웃 픽셀 참조)
# cv2.INTER_CUBIC - 3차 회선 보간법(4x4 이웃 픽셀 참마초)
# cv2.INTER_LANCZOS4 - Lanczos 보간법(8x8 이웃 픽셀 참조)
# cv2.INTER_AREA - 영상 축소 시 효과적

height,width,channel = re_img.shape
print(f"세로 : {height}, 가로 : {width}, 채널(RGB,GRAY,RGBA) : {channel}")

# 색상 공간 변경
# bgr_img = cv2.cvtColor(img1,cv2.COLOR_RGB2BGR)
# cv2.imshow("bgr",bgr_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 색상 변경
cv2.imshow("original",img1)
img1[30:40] = [255,0,255]
img1[:,10:20] = [0,255,0]
cv2.imshow("color change",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()