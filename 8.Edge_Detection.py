
import cv2
import numpy as np

# Function to display an image using OpenCV
def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the window after the key is pressed

# 1. Load the image
# 'cv2.IMREAD_GRAYSCALE' loads the image in grayscale mode
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found. Check the path!")
    exit()

display_image('Original Image', image)

# 2. Noise Reduction
# Apply Gaussian Blur to reduce noise. Kernel size (5, 5) and sigma=0 ensure proper smoothing.
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
display_image('Blurred Image', blurred_image)

# 3. Sobel Edge Detection
# Sobel calculates gradient in X and Y directions
# dx=1, dy=0 for horizontal edges, dx=0, dy=1 for vertical edges
# ksize=3 means a 3x3 kernel for Sobel operation (must be odd)
sobel_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges


# Convert results to uint8 for display
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

display_image('Sobel X', sobel_x)
display_image('Sobel Y', sobel_y)

# 4. Laplacian Edge Detection
# Laplacian detects edges by calculating the second derivative of the image.
# It is more sensitive to noise, so applying Gaussian Blur is essential.
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)  # Convert to uint8 for display
display_image('Laplacian Edge Detection', laplacian)

# 5. Canny Edge Detection
# Canny is a multi-step process:
# Step 1: Apply Gaussian Blur (already done).
# Step 2: Compute gradients and suppress non-maxima.
# Step 3: Apply double threshold to find strong and weak edges.
# Parameters:
# - threshold1: Lower bound for edge detection.
# - threshold2: Upper bound for edge detection.
edges = cv2.Canny(image, threshold1=50, threshold2=150)
display_image('Canny Edge Detection', edges)

# 6. Save the results
cv2.imwrite('sobel_x.jpg', sobel_x)
cv2.imwrite('sobel_y.jpg', sobel_y)
cv2.imwrite('laplacian.jpg', laplacian)
cv2.imwrite('canny_edges.jpg', edges)

print("Edge detection complete. Results saved as images.")
