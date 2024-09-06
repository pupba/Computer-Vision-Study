import cv2

image = cv2.imread("test.png")
image = cv2.resize(image,(int(image.shape[1]//2),int(image.shape[0]//2)),interpolation=cv2.INTER_LANCZOS4)
template = cv2.imread("template.png")
template = cv2.resize(template,(int(template.shape[1]//2),int(template.shape[0]//2)),interpolation=cv2.INTER_LANCZOS4)
h,w,_ = template.shape


# Template Matching
result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
# TM_CCOEFF: 상관 계수를 사용하여 매칭을 수행합니다. 값이 클수록 매칭이 잘 되는 것입니다.
# TM_CCOEFF_NORMED: 정규화된 상관 계수를 사용합니다. 결과 값은 0과 1 사이로, 1에 가까울수록 매칭이 잘 되는 것입니다.
# TM_CCORR: 상관을 사용하여 매칭합니다. 값이 클수록 매칭이 잘 되는 것입니다.
# TM_CCORR_NORMED: 정규화된 상관을 사용합니다. 결과 값은 0과 1 사이입니다.
# TM_SQDIFF: 제곱 차이를 계산하여 매칭합니다. 값이 작을수록 매칭이 잘 되는 것입니다.
# TM_SQDIFF_NORMED: 정규화된 제곱 차이를 사용합니다. 결과 값은 0과 1 사이로, 0에 가까울수록 매칭이 잘 되는 것입니다.

# 매칭 결과에서 최댓값과 위치를 찾는다.
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 템플릿의 위치를 사각형으로 그린다.
top_left = max_loc
bottom_right = (top_left[0]+w,top_left[1]+h)
cv2.rectangle(image,top_left,bottom_right,(0,255,0),2)

cv2.imshow("Template",template)
cv2.imshow("Template Matching",image)
cv2.waitKey(0)
cv2.destroyAllWindows()