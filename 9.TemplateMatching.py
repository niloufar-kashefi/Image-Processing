import cv2
import numpy as np


# Finding One Object==================================================================================================================================================
# Load the large image and template
image = cv2.imread('image.png', 0)
template = cv2.imread('template.png', 0)

# Find the template in the image
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Find the location with the highest similarity
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the matched template
top_left = max_loc
h, w = template.shape
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(image, top_left, bottom_right, 255, 2)

# Show the image with the matched templates
cv2.imshow('Matched Templates', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Finding One Object==================================================================================================================================================
# Load the large image and template
image = cv2.imread('image.png', 0)
template = cv2.imread('template.png', 0)

# Find the similarity
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Set the similarity threshold
threshold = 0.8
locations = np.where(result >= threshold)  # Find the coordinates of the matching locations
# (array([y axis value]), array([x axis value]))

# Create a list of found locations
points = list(zip(locations[1], locations[0]))  # Store the (x, y) coordinates

# Draw rectangles around all found locations
for x, y in points:
    cv2.rectangle(image, (x, y), (x + template.shape[1], y + template.shape[0]), 255, 1)

# Show the image with the matched templates
cv2.imshow('Matched Templates', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
