import cv2 
import numpy as np
from matplotlib import pyplot as plt
im = cv2.imread('cat3.jfif')
row,column = im.shape[:2]
kernal_x =cv2.getGaussianKernel(column,200)
kernal_y =cv2.getGaussianKernel(row,200)
kernal = kernal_y*kernal_x.T
filter = 255*kernal/np.linalg.norm(kernal)
vintage_im=np.copy(im)
for i in range (3):
    vintage_im [:,:,i]=vintage_im[:,:,i]*filter
plt.imshow(vintage_im) 
plt.show()   