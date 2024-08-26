import cv2

retval = cv2.VideoCapture("v1.mp4",apiPreference=None)
# 0 : 기본 카메라
# 1~ : 장치 관리자에 연결된 순서대로

# 카메라가 열렸는지 확인
if not retval.isOpened():
    print("실패!")
    import sys
    sys.exit()
# print("열기 성공")

# print(f"Width : {retval.get(cv2.CAP_PROP_FRAME_WIDTH)}")
# print(f"Height : {retval.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
# print(f"FPS : {retval.get(cv2.CAP_PROP_FPS)}")
retval.set(cv2.CAP_PROP_FRAME_WIDTH,480)
retval.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
while True:
    ret,frame = retval.read()
    
    if not ret: # 새로운 프레임을 못받아 왔을 때 break
        break

    # 영상 출력
    cv2.imshow("video",frame)

    # ESC 누르면 강제 종료
    if cv2.waitKey(10) == 27:
        break

retval.release() # 사용한 자원 해제
cv2.destroyAllWindows()