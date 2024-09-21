import cv2
import numpy as np

# 이미지 로드
img1 = cv2.imread('cat1.jpg', cv2.IMREAD_GRAYSCALE)  # 첫 번째 이미지
img2 = cv2.imread('cat2.jpg', cv2.IMREAD_GRAYSCALE)  # 두 번째 이미지

# SURF 객체 생성
surf = cv2.xfeatures2d.SURF_create(hessianThreshold=400)

# 특징점 검출 및 기술자 생성
keypoints1, descriptors1 = surf.detectAndCompute(img1, None)
keypoints2, descriptors2 = surf.detectAndCompute(img2, None)

# 매칭을 위한 BFMatcher 객체 생성
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# 특징점 매칭
matches = bf.match(descriptors1, descriptors2)

# 매칭 결과를 거리 기준으로 정렬
matches = sorted(matches, key=lambda x: x.distance)

# 매칭 결과 시각화
img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

print(f"NUmber of match result : {len(matches)}/{len(descriptors1)}")
# 결과 이미지 표시
cv2.imshow('Matches', img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
