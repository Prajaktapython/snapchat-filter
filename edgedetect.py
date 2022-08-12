import cv2 
import matplotlib.pyplot as plt
im = cv2.imread('cat3.jfif')
h=cv2.Canny(im,100,300)
plt.imshow (h)
plt.show()