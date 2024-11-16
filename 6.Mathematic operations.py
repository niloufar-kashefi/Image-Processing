import cv2
import numpy as np

# Load an image from file
# Replace 'image.jpg' with the path to your image
image = cv2.imread('image.png')

# If image is not loaded, exit
if image is None:
    raise ValueError("Image not found. Please provide a valid path.")

# ====================
# 1. Changing Color Space
# ====================
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Convert to HSV (Hue, Saturation, Value) color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display original and converted images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("HSV Image", hsv_image)

# ====================
# 2. Thresholding
# ====================
# Apply binary thresholding
_, binary_thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
# Explanation:
# cv2.threshold(src, thresh, maxval, type)
# - src: Input image (grayscale)
# - thresh: Threshold value
# - maxval: Maximum value to assign for pixels above the threshold
# - type: Type of thresholding (e.g., THRESH_BINARY)

cv2.imshow("Binary Threshold", binary_thresh)

# ====================
# 3. Resizing
# ====================
# Resize image to half its size
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
# Resize image to double its size
resized_image_double = cv2.resize(image, (image.shape[1] * 2, image.shape[0] * 2))

cv2.imshow("Resized Image (Half)", resized_image)
cv2.imshow("Resized Image (Double)", resized_image_double)

# ====================
# 4. Rotation
# ====================
# Rotate the image by 45 degrees
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
# Explanation:
# cv2.getRotationMatrix2D(center, angle, scale)
# - center: Rotation center point (x, y)
# - angle: Rotation angle in degrees
# - scale: Scaling factor
# cv2.warpAffine(src, M, dsize)
# - src: Input image
# - M: Transformation matrix (e.g., rotation_matrix)
# - dsize: Size of the output image

cv2.imshow("Rotated Image", rotated_image)

# ====================
# 5. Affine Transformation
# ====================
# Define points for affine transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

affine_matrix = cv2.getAffineTransform(pts1, pts2)
affine_transformed_image = cv2.warpAffine(image, affine_matrix, (cols, rows))
# Explanation:
# cv2.getAffineTransform(src_points, dst_points)
# - src_points: Source triangle points (3 points)
# - dst_points: Destination triangle points (3 points)

cv2.imshow("Affine Transformed Image", affine_transformed_image)

# ====================
# 6. Transformation (Translation)
# ====================
# Translate the image by 100 pixels to the right and 50 pixels down
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
# Explanation:
# Transformation matrix: [[1, 0, tx], [0, 1, ty]]
# - tx: Translation along x-axis
# - ty: Translation along y-axis

cv2.imshow("Translated Image", translated_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()



# Explanation of Functions:
# cv2.cvtColor(src, code)

# Converts an image from one color space to another.
# src: Input image.
# code: Conversion code, e.g., cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV.
# cv2.threshold(src, thresh, maxval, type)

# Applies a fixed-level threshold to a grayscale image.
# src: Grayscale input image.
# thresh: Threshold value.
# maxval: Maximum value to assign for pixels above the threshold.
# type: Thresholding type, e.g., cv2.THRESH_BINARY.
# cv2.resize(src, dsize)

# Resizes an image.
# src: Input image.
# dsize: Output size as a tuple (width, height).
# cv2.getRotationMatrix2D(center, angle, scale)

# Creates a 2D rotation matrix.
# center: Center of rotation.
# angle: Rotation angle in degrees.
# scale: Scaling factor.
# cv2.getAffineTransform(src_points, dst_points)

# Calculates the affine transformation matrix.
# src_points: 3 points in the source image.
# dst_points: 3 points in the destination image.
# cv2.warpAffine(src, M, dsize)

# Applies an affine transformation to an image.
# src: Input image.
# M: Transformation matrix.
# dsize: Output image size.
# This code demonstrates how to use OpenCV for basic mathematical transformations and provides comments for clarity.