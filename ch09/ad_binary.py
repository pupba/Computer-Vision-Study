import cv2

if __name__ == "__main__":
    im = cv2.imread("test.png")
    shape = (int(im.shape[1] * 0.5), int(im.shape[0] * 0.5))
    im = cv2.resize(im,shape)
    cv2.imshow("Origin",im)
    gim = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # 적응형 이진화
    adp = cv2.adaptiveThreshold(gim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imshow("AdaptiveThreshold",adp)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    