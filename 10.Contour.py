import cv2  # Import the OpenCV library
import numpy as np  # Import NumPy for numerical operations

# Step 1: Load the image
# cv2.imread(filename, flags): Loads an image from a file
# - filename: Path to the image file
# - flags: Specifies the color type of a loaded image (default is cv2.IMREAD_COLOR)
# Returns: The loaded image as a NumPy array
image = cv2.imread('image.jpg')

# Step 2: Convert the image to grayscale
# cv2.cvtColor(src, code): Converts an image from one color space to another
# - src: Input image
# - code: Color space conversion code (e.g., cv2.COLOR_BGR2GRAY)
# Returns: Grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply a threshold
# cv2.threshold(src, thresh, maxval, type): Applies a fixed-level threshold to an image
# - src: Input grayscale image
# - thresh: Threshold value
# - maxval: Maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types
# - type: Thresholding type (e.g., cv2.THRESH_BINARY)
# Returns: A tuple of the threshold value used and the binary thresholded image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Step 4: Find contours
# cv2.findContours(image, mode, method): Detects contours in a binary image
# - image: Input binary image (usually from thresholding or edge detection)
# - mode: Contour retrieval mode (e.g., cv2.RETR_TREE retrieves all contours and reconstructs a full hierarchy)
# - method: Contour approximation method (e.g., cv2.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments)
# Returns: A tuple of contours and the hierarchy
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Draw the contours
# cv2.drawContours(image, contours, contourIdx, color, thickness): Draws contours on an image
# - image: Input image on which to draw
# - contours: List of contours to draw (from cv2.findContours)
# - contourIdx: Index of the contour to draw (-1 means all contours)
# - color: Color of the contour lines (e.g., (0, 255, 0) for green)
# - thickness: Thickness of the contour lines (e.g., 2 for a line of 2 pixels)
# Returns: The image with contours drawn on it
contoured_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

# Step 6: Display the original and contoured images
# cv2.imshow(winname, mat): Displays an image in a window
# - winname: Name of the window
# - mat: Image to be displayed
# Note: Windows created by OpenCV are interactive and allow resizing, closing, etc.
cv2.imshow('Original Image', image)
cv2.imshow('Contours', contoured_image)

# Step 7: Wait for a key press and close the windows
# cv2.waitKey(delay): Waits for a specified amount of time for a key event
# - delay: Delay in milliseconds (0 means indefinite wait)
# cv2.destroyAllWindows(): Closes all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the contoured image to a file
# cv2.imwrite(filename, img): Saves an image to a specified file
# - filename: Name of the file to save the image to
# - img: Image to save
# Returns: True if the image is successfully written, False otherwise
cv2.imwrite('contoured_image.jpg', contoured_image)