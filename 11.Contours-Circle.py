import cv2
import numpy as np

# Load the image
image = cv2.imread('image_with_circles.jpg', cv2.IMREAD_COLOR)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a blur to reduce noise and improve circle detection
gray = cv2.GaussianBlur(gray, (15, 15), 0)

# Use HoughCircles to detect circles
circles = cv2.HoughCircles(
    gray, 
    cv2.HOUGH_GRADIENT, dp=1.2, minDist=50, param1=50, param2=40, minRadius=10, maxRadius=100
)

# If circles are detected
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")  # Convert float to int
    # Print number of circles detected
    print(f"Number of circles detected: {len(circles)}")
    for (x, y, r) in circles:
        # Draw the outer circle
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        # Draw the center of the circle
        cv2.circle(image, (x, y), 3, (0, 0, 255), 3)

# Show the image with detected circles
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()