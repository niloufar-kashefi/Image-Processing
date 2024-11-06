import cv2
import numpy as np

# Load two images
img1 = cv2.imread('image.png')  # Replace with your image path
img2 = cv2.imread('output_shapes.jpg')  # Replace with your second image path

# 1. Displaying Image Properties for img1
print("Image 1 Shape (Height, Width, Channels):", img1.shape)
print("Image 1 Data Type:", img1.dtype)

# Displaying Image Properties for img2
print("Image 2 Shape (Height, Width, Channels):", img2.shape)
print("Image 2 Data Type:", img2.dtype)

# 2. Checking if the two images have the same size
# If not, resize img2 to match img1's size
if img1.shape != img2.shape:
    print("Resizing Image 2 to match Image 1 dimensions.")
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  # Resize img2 to img1's width and height

# # 3. Region of Interest (ROI)
# roi = img2[50:150, 50:150]  # Define ROI in img1
# cv2.imshow('Region of Interest', roi)


# # 4.a. Editing Image Pixel
# # Example: Turn all pixels in the ROI to red
# img1[50:150, 50:150] = [0, 0, 255]  # Setting the region to red
# cv2.imshow('Edited Image with Red ROI', img1)



# # 4.b. Editing Image Pixel
# # Example: line ROI
# for i in range(300):
#     img1[i,i] = [0, 0, 255]  # Setting the region to red
# cv2.imshow('Edited Image with Red ROI', img1)


# # 5. Copying and Pasting Part of an Image to Another Part
# # Define the source ROI from img1
# src_part = img1[50:150, 50:150]  # A 100x100 region from (50,50)

# # Define the destination position to paste the ROI in img1
# # Here we’ll paste the ROI at a different location, say (200, 200)
# img1[200:300, 200:300] = src_part
# cv2.imshow('Image with Copied Part', img1)



# # 6. Adding Borders with cv2.copyMakeBorder
# blue_border = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 0, 0])
# cv2.imshow('Constant Blue Border', blue_border)

# reflect_border = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
# cv2.imshow('Reflect Border', reflect_border)

# wrap_border = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
# cv2.imshow('Wrap Border', wrap_border)

# replicate_border = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
# cv2.imshow('Replicate Border', replicate_border)


# # Merging channels / Adding two image / Blending two image----------------------------------------------------

# # Splitting and Merging Channels
# b1, g1, r1 = cv2.split(img1)
# b2, g2, r2 = cv2.split(img2)

# # Merge channels from img1 and img2
# merged_img = cv2.merge((b1, g1, r1))  # Using Blue from img1, Green from img2, and Red from img1
# cv2.imshow('Merged Image from Two Pictures', merged_img)


# # Adding Images Together: 1. img1 + img2 /// 2. cv2.add(img1,img2)
# # NOTE: Images must have the same size

# added_img = img1 + img2  # Adds each pixel value
# cv2.imshow('Added Images with +', added_img)


# # Perform pixel addition with cv2.add()
# added_img = cv2.add(img1, img2)  # Adds each pixel value; makes the result brighter
# cv2.imshow('Added Images with add', added_img)

# # 9. Blending Images with cv2.addWeighted
# alpha = 0.5  # Weight of the first image
# beta = 0.5   # Weight of the second image
# blended_img = cv2.addWeighted(img1, alpha, img2, beta, 0)
# cv2.imshow('Blended Images', blended_img)

cv2.waitKey(0)
cv2.destroyAllWindows()










# ##Tutorial-------------------------------------------------------------------------------
# img.shape: Retrieves the dimensions of the image.
# img.dtype: Retrieves the data type of the image.
# cv2.split and cv2.merge: Used for separating and combining image channels.
# cv2.copyMakeBorder: Adds borders around images with multiple border styles.
# cv2.add: Adds pixel values of two images, making the result brighter.
# cv2.addWeighted: Blends two images with specified weights for each image.
# cv2.resize: This function is introduced to resize img2 to the same width and height as img1. The cv2.resize function takes two arguments: the image to resize and a tuple specifying the desired width and height.