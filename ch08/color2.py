import cv2

if __name__ == "__main__":
    img = cv2.imread("test.png",cv2.IMREAD_COLOR)
    img = cv2.resize(img,(512,600),interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("Origin",img)

    cv2.imshow("RGB",cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    cv2.imshow("Gray",cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
    cv2.waitKey(0)
    cv2.destroyAllWindows()