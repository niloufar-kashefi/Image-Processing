import cv2
import numpy as np

# Step 1: Create a black image with 3 color channels (RGB) - 300x300 pixels
image1 = np.zeros((300, 300, 3), dtype=np.uint8)

# Step 2: Draw a blue rectangle on the first image
# The rectangle color is blue (B=255, G=0, R=0)
cv2.rectangle(image1, (50, 50), (250, 250), (255, 0, 0), -1)

# Step 3: Create another black image with 3 color channels
image2 = np.zeros((300, 300, 3), dtype=np.uint8)

# Step 4: Draw a green circle on the second image
# The circle color is green (B=0, G=255, R=0)
cv2.circle(image2, (150, 150), 100, (0, 255, 0), -1)

# Step 5: Perform bitwise operations

# Bitwise AND - Only the overlapping regions with colors will appear
bitwise_and = cv2.bitwise_and(image1, image2)

# Bitwise OR - Combines the colored areas of both shapes
bitwise_or = cv2.bitwise_or(image1, image2)

# Bitwise XOR - Keeps the non-overlapping colored areas
bitwise_xor = cv2.bitwise_xor(image1, image2)

# Bitwise NOT - Inverts the colors for the first image
bitwise_not_image1 = cv2.bitwise_not(image1)

# Bitwise NOT - Inverts the colors for the second image
bitwise_not_image2 = cv2.bitwise_not(image2)

# Step 6: Display all results
cv2.imshow("Rectangle (Blue)", image1)
cv2.imshow("Circle (Green)", image2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT - Rectangle", bitwise_not_image1)
cv2.imshow("Bitwise NOT - Circle", bitwise_not_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Bitwise AND
# Description: The Bitwise AND operation keeps only the overlapping area where both shapes have color.
# Result: Only the intersecting part of the two shapes remains visible, and it shows in the combined color if the shapes are colored. For example, if there’s a blue rectangle and a green circle, the overlapping area might appear as a mix of those colors, depending on the channel intensities.
# Bitwise OR
# Description: The Bitwise OR operation combines both shapes, displaying every area where at least one of the shapes has color.
# Result: Both shapes appear with their original colors. Any pixel that’s colored in either image will be shown in the result, so all visible areas of both shapes are combined into one image.
# Bitwise XOR
# Description: The Bitwise XOR operation keeps only the non-overlapping areas of the two shapes.
# Result: Only the unique, non-overlapping parts of each shape are shown, while the intersecting (overlapping) area becomes black (or empty). This operation highlights the distinct parts of each shape, excluding any shared pixels.
# Bitwise NOT
# Description: The Bitwise NOT operation inverts the colors of the image.
# Result: All black (0, 0, 0) pixels turn white (255, 255, 255), and any colored pixels change to their complementary color. For example, green (0, 255, 0) would become magenta (255, 0, 255). This inversion is done separately for each image, so each shape’s color changes to its opposite.