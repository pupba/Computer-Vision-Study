import cv2

color_img = cv2.imread("test.jpg",cv2.IMREAD_COLOR)
gray_img = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
color_alpha_img = cv2.imread("test.jpg",cv2.IMREAD_UNCHANGED)

cv2.imshow("color",color_img)
cv2.imshow("gray",gray_img)
cv2.imshow("color_alpha",color_alpha_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("color.jpg",color_img)
cv2.imwrite("gray.jpg",gray_img)
cv2.imwrite("alpha.png",color_alpha_img)
