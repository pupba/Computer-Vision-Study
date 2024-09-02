import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
    cv2.imshow("origin",img)

    # sobel 필터 적용
    sobel_x = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=3) # 수평 에지
    cv2.imshow("x_edge",sobel_x)
    sobel_y = cv2.Sobel(img,cv2.CV_32F,0,1,ksize=3) # 수직 에지
    cv2.imshow("y_edge",sobel_y)
    # edge 합치기
    edges = cv2.magnitude(sobel_x,sobel_y)
    # 정규화
    edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Thresholding (에지 강조)
    _, edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("edge",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()