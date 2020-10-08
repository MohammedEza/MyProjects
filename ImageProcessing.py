import cv2
import numpy as np
image = cv2.imread('Image.jpg')
#print(image) #image is displayed as array of pixel intensity.
work_image = np.copy(image) #Copy created
work_image = cv2.cvtColor(work_image,cv2.COLOR_RGB2GRAY)
work_image = cv2.flip(work_image,1)
cv2.imwrite('Processed.jpg',work_image)
cv2.imshow('Processed_Image',work_image)
cv2.waitKey(0)