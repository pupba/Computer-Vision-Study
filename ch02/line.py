import cv2
import numpy as np

# 흰배경의 빈 이미지 생성(512 x 512)

white_background = np.ones((512,512),dtype=np.uint8) * 255

# 직선
# cv2.line(
#     img=white_background,
#     pt1=(0,0),
#     pt2=(256,256),
#     color=(100,200,0),
#     thickness=3,
#     lineType=cv2.LINE_4,
#     shift=0)
# cv2.imshow("line",white_background)

# 화살표
# cv2.arrowedLine(
#     img=white_background,
#     pt1=(0,0),
#     pt2=(256,256),
#     color=(100,200,100),
#     thickness=3,
#     line_type=cv2.LINE_AA,
#     shift=0,
#     tipLength=0.2
# )
# cv2.imshow("arrow",white_background)
# 마커
cv2.drawMarker(
    img=white_background,
    position=(50,50),
    color=0,
    markerType=cv2.MARKER_DIAMOND,
    markerSize=20,
    thickness=3,
    line_type=cv2.LINE_8
)
cv2.imshow("Marker",white_background)
cv2.waitKey(0)
cv2.destroyAllWindows()