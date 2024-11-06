import cv2
import numpy as np
import os

#imageVarName=cv2.imread("Image dir and name",cv2.typeOfRead)  #typeOfRead: IMREAD_COLOR or 1 , IMREAD_GRAYSCALE or 0
#cv2.imshow("imageWindowName",imageVarName)
#cv2.imwrite("newImageName.newFormat",imageVarName)

image_path = 'D:/Project-Python/OpenCV/image.png'

# Check Path
if not os.path.exists(image_path):
    print(f"Error: The file at {image_path} does not exist.")
else:
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  #1 is color, 0 is gray


if img is None:
    print("Error: Could not read image.")
else:
    cv2.imshow('Image', img)


cv2.imwrite("new.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()   #release memory