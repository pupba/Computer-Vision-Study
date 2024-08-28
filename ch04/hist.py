import cv2
import matplotlib.pyplot as plt
if __name__ == "__main__":
    # image = cv2.imread("test.png",cv2.IMREAD_GRAYSCALE)
    # plt.hist(image.ravel(),256,[0,256])
    # plt.show()

    image = cv2.imread("test.png")
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr,color=col)
        plt.xlim([0,256])
    plt.show()
