import cv2

if __name__ == "__main__":
    im = cv2.imread("test.png")
    shape = (int(im.shape[1] * 0.5), int(im.shape[0] * 0.5))
    im = cv2.resize(im,shape)
    cv2.imshow("Origin",im)
    gim = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    
    # 침식
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) # (5x5)
    eroded = cv2.erode(gim,kernel=kernel,iterations=1)
    cv2.imshow("Eroded",eroded)
    # 팽창
    dilated = cv2.dilate(gim,kernel=kernel,iterations=1)
    cv2.imshow("Dilated",dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()