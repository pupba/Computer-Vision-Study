import cv2
import numpy as np
# affine
from transforms import transformation,transformation_per

def show(origin:np.ndarray,result:np.ndarray):
    cv2.imshow("origin",origin)
    cv2.imshow("result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("test.png")
img = cv2.resize(img,(480,480))

# points_src = np.float32([[50, 50], [200, 50], [50, 200]])
# points_dst = np.float32([[10, 100], [200, 50], [100, 250]])
# matrix = cv2.getAffineTransform(points_src,points_dst)

# result = transformation(img,matrix,img.shape[:2])
# tx = 100 # x축으로 이동할 거리
# ty = 50 # y축으로 이동할 거리
# matrix = np.float32([[1,0,tx],[0,1,ty]])
# result = transformation(img,matrix,img.shape[:2])

# # 전단 변환 행렬 설정 (x축으로 0.5의 전단)
# shear_factor = 0.5
# matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])
# shape = img.shape[:2]
# result = transformation(img,matrix,(int(shape[0]+shape[1] * shear_factor),shape[1]))

# result = cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LANCZOS4)

# # 회전 축 좌표
# h,w,_ = img.shape
# center = (h // 2,w // 2)
# # 회전 각도
# angle = 45
# # 변호나 행렬
# matrix = cv2.getRotationMatrix2D(center,angle,1.0) # 마지막 인자는 스케일링
# result = transformation(img,matrix,(w,h))

# show(img,result)
# cv2.imshow("origin",img)
# # 수평 대칭 (X축 기준)
# horizontal_flip = cv2.flip(img, 0)
# cv2.imshow("horizon",horizontal_flip)
# # 수직 대칭 (Y축 기준)
# vertical_flip = cv2.flip(img, 1)
# cv2.imshow("vertical",vertical_flip)
# # 중심 대칭 (원점 기준)
# both_flip = cv2.flip(img, -1)
# cv2.imshow("both",both_flip)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 원본 이미지에서 변환할 네 점 (시작점)
points = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# 변환할 네 점 (대상점)
dst_points = np.float32([[10, 10], [300, 50], [50, 250], [250, 200]])

# 투시 변환 행렬 생성
matrix = cv2.getPerspectiveTransform(points, dst_points)

# 이미지에 투시 변환 적용
height, width = img.shape[:2]
result = cv2.warpPerspective(img, matrix, (width, height))
show(img,result)

