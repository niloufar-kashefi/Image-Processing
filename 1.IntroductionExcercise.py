import cv2
import numpy as np 

image = cv2.imread("D:/Project-Python/OpenCV/image.png", cv2.IMREAD_COLOR)

cv2.line(image, (50, 50), (400, 50), (255, 0, 0), 5)

cv2.imwrite("newImageName.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows() 