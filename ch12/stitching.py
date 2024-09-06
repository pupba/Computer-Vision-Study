import cv2

# 이미지 읽기
img1 = cv2.imread('cat1.png')
img1 = cv2.resize(img1,(int(img1.shape[1]//2),int(img1.shape[0]//2)),interpolation=cv2.INTER_LANCZOS4)
img2 = cv2.imread('cat2.png')
img2 = cv2.resize(img2,(int(img2.shape[1]//2),int(img2.shape[0]//2)),interpolation=cv2.INTER_LANCZOS4)
img3 = cv2.imread('cat3.png')
img3 = cv2.resize(img3,(int(img3.shape[1]//2),int(img3.shape[0]//2)),interpolation=cv2.INTER_LANCZOS4)

img_list = [img1,img2,img3]

stitcher = cv2.Stitcher.create()

status,stitched = stitcher.stitch(img_list)
# 결과 이미지 출력
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
cv2.imshow("Stiched Image",stitched)
cv2.waitKey(0)
cv2.destroyAllWindows()