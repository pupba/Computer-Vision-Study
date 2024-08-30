import cv2
import numpy as np
def transformation(image:np.ndarray,matrix:np.ndarray,shape:tuple):
    return cv2.warpAffine(image,matrix,shape)

def transformation_per(image:np.ndarray,matrix:np.ndarray,shape:tuple):
    return cv2.warpPerspective(image,matrix,shape)