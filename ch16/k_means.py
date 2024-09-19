import cv2
import numpy as np
import random

if __name__ == "__main__":
    img = cv2.imread("cat.png")
    # Resize
    h,w,c = img.shape
    img = cv2.resize(img,(int(w//2),int(h//2)))
    cv2.imshow("original",img)

    # BGR to RGB
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # 이미지를 2D 배열로 변환
    pixel_values = img.reshape((-1,3))
    pixel_values = np.float32(pixel_values)
    # k-means
    k = 2
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100,0.2)
    # Radom으로 중앙 설정
    _,labels,centers = cv2.kmeans(pixel_values,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # 각 클러스터에 대해 랜덤 색상 생성
    colors = []
    for _ in range(k):
        colors.append([random.randint(0, 255) for _ in range(3)])

    # 세그멘테이션된 이미지를 색상으로 채우기
    segmented_img = np.zeros_like(img)
    for i in range(len(labels)):
        segmented_img[i // img.shape[1], i % img.shape[1]] = colors[labels[i][0]]

    cv2.imshow("segmentation",segmented_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()