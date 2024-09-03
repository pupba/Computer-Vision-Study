import cv2

if __name__ == "__main__":
    im = cv2.imread("test.png")
    shape = (int(im.shape[1] * 0.5), int(im.shape[0] * 0.5))
    im = cv2.resize(im,shape)
    cv2.imshow("Origin",im)
    gim = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # 고정 임계값
    _, b_fix = cv2.threshold(gim,120,255,cv2.THRESH_BINARY)
    cv2.imshow("Fix Binary",b_fix)
    # Otsu를 사용하여 자동으로 최적의 임계값 계싼
    _, b_otsu = cv2.threshold(gim,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("Otsu Binary",b_otsu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    