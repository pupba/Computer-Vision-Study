import cv2
import numpy as np

if __name__ == "__main__":
    # 이미지 읽기
    img = cv2.imread("test3.jpg")
    cv2.imshow("Original Image", img)

    # 그레이스케일 변환
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny 엣지 검출
    edges = cv2.Canny(img_g, 50, 150)

    # 허프 변환을 사용하여 원 검출 (엣지 이미지 사용)
    circles = cv2.HoughCircles(edges, 
                                cv2.HOUGH_GRADIENT, 
                                dp=1, 
                                minDist=30,  # 원 간의 최소 거리 조정
                                param1=50,  # Canny 엣지 검출의 상한값 조정
                                param2=30,   # 원 검출의 임계값 조정
                                minRadius=10, # 최소 반지름 조정
                                maxRadius=100) # 최대 반지름 조정

    # 원 그리기
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # 원의 중심 그리기
            cv2.circle(img, (i[0], i[1]), 5, (0, 255, 0), -1)
            # 원 그리기
            cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)

    # 결과 이미지 표시
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("Detected Circles", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
