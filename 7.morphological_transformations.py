
# Import necessary libraries
import cv2
import numpy as np

# Load the input image in grayscale mode
# Replace 'image.png' with the path to your image
image = cv2.imread('image.jpg', 0)

# Define a kernel (structuring element)
# Kernel is a small matrix used to define the neighborhood for the operations
kernel = np.ones((3, 3), np.uint8)  # A 3x3 matrix with all ones

# Erosion: Shrinks bright regions in the image
# Parameters: 
# - src: Input image
# - kernel: Structuring element
# - iterations: Number of times the operation is applied
eroded = cv2.erode(image, kernel, iterations=1)

# Dilation: Expands bright regions in the image
dilated = cv2.dilate(image, kernel, iterations=1)

# Opening: Erosion followed by Dilation, used to remove small objects
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing: Dilation followed by Erosion, used to fill small holes
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient: Difference between Dilation and Erosion
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Top Hat: Difference between the original image and its opening
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Black Hat: Difference between the closing of the image and the original
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display results
# Each operation's result is displayed in a separate window
cv2.imshow('Original', image)
cv2.imshow('Erosion', eroded)
cv2.imshow('Dilation', dilated)
cv2.imshow('Opening', opened)
cv2.imshow('Closing', closed)
cv2.imshow('Gradient', gradient)
cv2.imshow('Top Hat', tophat)
cv2.imshow('Black Hat', blackhat)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
