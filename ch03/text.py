import cv2
im = cv2.imread("test.png")

text ="rabbit"
cv2.putText(
    img=im,
    text=text,
    org=(50,50),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1,
    color=(242,200,100),
    thickness=1,
    lineType=cv2.LINE_AA,
    bottomLeftOrigin=False
)
cv2.imshow("text",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
