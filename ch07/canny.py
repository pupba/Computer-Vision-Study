import cv2

if __name__ == "__main__":
    img = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
    cv2.imshow("origin",img)
    canny = cv2.Canny(img,threshold1=100,threshold2=200)
    cv2.imshow("canny",canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()