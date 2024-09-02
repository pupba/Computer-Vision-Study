import cv2
import numpy as np
if __name__ == "__main__":
    img = cv2.imread("test2.jpg")
    cv2.imshow("origin",img)

    img_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img_g,50,150)

    lines = cv2.HoughLinesP(edges,1,np.pi / 180, threshold=100,minLineLength=50,maxLineGap=10)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 초록색으로 직선 그리기
    
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("Detected Lines", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()