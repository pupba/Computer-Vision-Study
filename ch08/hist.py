import cv2

if __name__ == "__main__":
    img = cv2.imread("test.png",cv2.IMREAD_COLOR)
    img = cv2.resize(img,(512,600),interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("Origin",img)

    b,g,r = cv2.split(img)
    b_h = cv2.equalizeHist(b)
    g_h = cv2.equalizeHist(g)
    r_h = cv2.equalizeHist(r)

    eh_img = cv2.merge([b_h,g_h,r_h])

    cv2.imshow("Histogram Equalized Image",eh_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()