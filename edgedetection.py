import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread(r'temp1.png',0)
img=cv2.imread(r'messi5.jpg',0)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))
sobel_add=cv2.bitwise_or(sobelX,sobelY)
#_,mask=cv2.threshold(sobel_add,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)
dia=cv2.morphologyEx(sobel_add,cv2.MORPH_OPEN,kernal)
titles=['image','lap','sobelX','sobelY','sobel_or','ker']
images=[img,lap,sobelX,sobelY,sobel_add,dia]
for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
