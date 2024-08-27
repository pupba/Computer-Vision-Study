import cv2
import numpy as np

background = np.zeros((512,512,3),dtype=np.uint8) # RGB 채널

# 사각형
# cv2.rectangle(
#     img=background,
#     pt1 = (50,50),
#     pt2 = (250,250),
#     color=(255,0,0),
#     thickness=1,
#     lineType=cv2.LINE_AA,
#     shift=0
# )
# cv2.imshow("rectangle",background)

# 원
# cv2.circle(
#     img=background,
#     center=(256,256),
#     radius=50,
#     color=(0,255,0),
#     thickness=3,
#     lineType=cv2.LINE_8,
#     shift=0
# )
# cv2.imshow("circle",background)

# 타원
# cv2.ellipse(
#     img=background,
#     center=(256,256),
#     axes=(170,100),
#     angle=0,
#     startAngle=0,
#     endAngle=360,
#     color=(0,255,100),
#     thickness=3,
#     lineType=cv2.LINE_AA,
#     shift=0
# )
# cv2.imshow("ellipse",background)

# 다각형
points = np.array([[[10,10],[170,10],[200,230],[70,70],[50,150]]],dtype=np.int32)

# cv2.polylines(
#     img=background,
#     pts=points,
#     isClosed=True,
#     color=(255,255,0),
#     thickness=2,
#     lineType=cv2.LINE_AA,
#     shift=0
# )
# cv2.imshow("polylines",background)

# 볼록 다각형
cv2.fillConvexPoly(
    img=background,
    points=points,
    color=(102,100,24),
    lineType=cv2.LINE_8,
    shift=0
)
cv2.imshow("fill Poly",background)

cv2.waitKey(0)
cv2.destroyAllWindows()