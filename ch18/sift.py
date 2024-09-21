import cv2

# 이미지 읽기
image1 = cv2.imread('cat1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('rabbit1.jpg', cv2.IMREAD_GRAYSCALE)

# SIFT 객체 생성
sift = cv2.SIFT_create()

# 특징점 및 디스크립터 추출
keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

# 매칭을 위한 BFMatcher 생성
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# 특징점 매칭
matches = bf.match(descriptors1, descriptors2)

# 매칭 결과 정렬
matches = sorted(matches, key=lambda x: x.distance)

# 매칭 결과 시각화
result_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches, None)

print(f"NUmber of match result : {len(matches)}/{len(descriptors1)}")

# 결과 이미지 출력
cv2.imshow('SIFT Matches', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()