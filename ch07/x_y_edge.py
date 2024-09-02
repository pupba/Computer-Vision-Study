import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
    cv2.imshow("origin",img)
    x_mask = np.array([-1,0,1])
    y_mask = np.array([[-1],[0],[1]])

    x_edge = cv2.filter2D(img,-1,x_mask)
    cv2.imshow("x_edge",x_edge)
    y_edge = cv2.filter2D(img,-1,y_mask)
    cv2.imshow("y_edge",y_edge)
    # edge 합치기
    edges = cv2.magnitude(x_edge.astype(np.float32), y_edge.astype(np.float32))

    cv2.imshow("edge",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()