import cv2
img = cv2.imread("test.png",cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(512,512),interpolation=cv2.INTER_LANCZOS4)

def on_change(pos:int):
    _,binary = cv2.threshold(img,pos,255,cv2.THRESH_BINARY)
    cv2.imshow("thres",binary)
cv2.imshow("thres",img)
cv2.createTrackbar("Threshold Controler","thres",100,125,on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()