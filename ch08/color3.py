import cv2

if __name__ == "__main__":
    img = cv2.imread("test.png",cv2.IMREAD_COLOR)
    img = cv2.resize(img,(512,600),interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("Origin",img)
    b,g,r = cv2.split(img)
    cv2.imshow("Blue",b)
    cv2.imshow("Green",g)
    cv2.imshow("Red",r)
    me = cv2.merge([b,g,r])
    cv2.imshow("Merged",me)
    cv2.waitKey(0)
    cv2.destroyAllWindows()