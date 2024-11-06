import cv2
import numpy as np

# Step 1: Create a black image using NumPy
# We create a 300x300 pixel image filled with zeros (black).
image1 = np.zeros((300, 300), dtype=np.uint8)

# Step 2: Draw a white rectangle on the first image
# The rectangle goes from coordinates (50, 50) to (250, 250).
# 255 is the color intensity for white in grayscale, and -1 fills the shape.
cv2.rectangle(image1, (50, 50), (250, 250), 255, -1)

# Step 3: Create a second black image of the same size
image2 = np.zeros((300, 300), dtype=np.uint8)

# Step 4: Draw a white circle on the second image
# The circle is centered at (150, 150) with a radius of 100 pixels.
cv2.circle(image2, (150, 150), 100, 255, -1)

# Step 5: Perform bitwise operations

# Bitwise AND - Only the overlapping white regions will remain white.
bitwise_and = cv2.bitwise_and(image1, image2)

# Bitwise OR - Combines the white areas of both shapes.
bitwise_or = cv2.bitwise_or(image1, image2)

# Bitwise XOR - Keeps the non-overlapping white areas.
bitwise_xor = cv2.bitwise_xor(image1, image2)

# Bitwise NOT - Inverts the colors (black to white and white to black) for the first image.
bitwise_not_image1 = cv2.bitwise_not(image1)

# Bitwise NOT - Inverts the colors for the second image.
bitwise_not_image2 = cv2.bitwise_not(image2)

# Step 6: Display all the results
cv2.imshow("Rectangle", image1)
cv2.imshow("Circle", image2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT - Rectangle", bitwise_not_image1)
cv2.imshow("Bitwise NOT - Circle", bitwise_not_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Explanation of the Code
# Creating the Base Images: We start by creating two black images (300x300 pixels) using np.zeros. This will serve as a background.

# Drawing Shapes: We draw a white rectangle on image1 and a white circle on image2. These shapes help us see the effects of bitwise operations.

# Bitwise Operations:

# Bitwise AND: Keeps only the area where both shapes overlap. Both pixels need to be white for this to appear white in the result.
# Bitwise OR: Combines the white areas of both images. Any pixel that’s white in either image will be white in the result.
# Bitwise XOR: Keeps only the non-overlapping areas, creating a boundary effect.
# Bitwise NOT: Inverts colors for each image individually. Black areas become white, and white areas become black.
# Each operation shows a different way of combining or modifying the images.




