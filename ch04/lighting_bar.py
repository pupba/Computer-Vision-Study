import cv2
import numpy as np
img = np.zeros((480,480),np.uint8)
now = 0
def lighting(brightness: int) -> None:
    global img, now
    delta = brightness - now
    
    # 밝기 조정
    if delta > 0:
        img = cv2.add(img, delta)
    elif delta < 0:
        img = cv2.subtract(img, -delta)
    now = brightness

    cv2.imshow("lighting_bar", img)

if __name__ == "__main__":
    cv2.imshow("lighting_bar",img)
    cv2.createTrackbar("Control","lighting_bar",now,255,lighting)
    cv2.waitKey(0)
    cv2.destroyAllWindows()