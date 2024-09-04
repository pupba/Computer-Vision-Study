import cv2
import random

# 이미지 로드
image = cv2.imread('test.png')
if image is None:
    print("이미지를 로드할 수 없습니다.")
    exit()
sp = image.shape
image = cv2.resize(image,(int(sp[1]*0.5),int(sp[0]*0.5)),cv2.INTER_LANCZOS4)

# 그레이스케일 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진화
_, thresh = cv2.threshold(gray, 162, 255, cv2.THRESH_BINARY)
cv2.imshow("thres",thresh)

# 연결된 컴포넌트 찾기
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity=8)

# 바운딩 박스 그리기
for i in range(1, num_labels):  # 0은 배경이므로 1부터 시작
    # 바운딩 박스 정보
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]

    # 랜덤 색상 생성
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 바운딩 박스 그리기
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    # 중심점 계산
    cX = int(centroids[i, 0])
    cY = int(centroids[i, 1])

# 결과 이미지 출력
cv2.imshow('Labeled Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
