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

# Display the original image
display_image('Original Image', image)

# 2. Histogram Calculation (before CLAHE or Equalization)
# Calculate the histogram of the image using cv2.calcHist
# 'image' is the source image, [0] specifies the grayscale channel (0 for single channel images like grayscale),
# [256] specifies the number of bins (pixel intensity values from 0 to 255).
hist = cv2.calcHist([image], [0], None, [256], [0, 256])


# 3. Histogram Equalization
# This process enhances the contrast of the image by spreading out the most frequent intensity values.
equalized_image = cv2.equalizeHist(image)
display_image('Equalized Image', equalized_image)

# 4. Histogram after Equalization
# Recalculate the histogram of the equalized image
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])


# 5. CLAHE (Contrast Limited Adaptive Histogram Equalization)
# Create CLAHE object with specific parameters
# clipLimit controls the contrast enhancement, and tileGridSize defines the size of the grid.
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Apply CLAHE to the image
clahe_image = clahe.apply(image)
display_image('CLAHE Image', clahe_image)

# 6. Histogram after CLAHE
# Recalculate the histogram of the CLAHE image
hist_clahe = cv2.calcHist([clahe_image], [0], None, [256], [0, 256])

# Print the histogram values for the CLAHE image
print("Histogram values (CLAHE):")
print(hist_clahe)

# 7. Save the results
cv2.imwrite('equalized_image.jpg', equalized_image)
cv2.imwrite('clahe_image.jpg', clahe_image)



# cv2.calcHist():
# image: This is the input image for which the histogram will be calculated.
# [0]: This specifies the channel. For grayscale images, we use channel 0.
# None: This means no mask is applied to the image.
# [256]: This is the number of bins for the histogram (from 0 to 255 intensity values for grayscale images).
# [0, 256]: This specifies the range of intensity values (from 0 to 255 for grayscale images).


# cv2.equalizeHist():
# This function performs histogram equalization to improve the contrast of the image by spreading out the most frequent intensity values.


# cv2.createCLAHE(clipLimit, tileGridSize):
# clipLimit: The maximum contrast limit for each block. Larger values enhance the contrast more.
# tileGridSize: Specifies the grid size to divide the image into smaller blocks. Smaller grid sizes provide better local enhancement. A typical value is (8, 8) or (16, 16).

# clahe.apply(image):
# This function applies the CLAHE algorithm to the image, improving local contrast and preserving local details.