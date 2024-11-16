import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale mode
# Make sure you have an image named 'input_image.jpg' in your working directory or update the filename
image = cv2.imread('input_image.jpg', 0)  # Grayscale image for simplicity

# -------------------------------------------------------------------------------------------------------------
# 1. Mean Filter
# -------------------------------------------------------------------------------------------------------------
# The Mean Filter (or Average Filter) smooths an image by averaging the pixel values within a defined kernel/window.
# Each pixel is replaced with the average value of its neighboring pixels within the kernel size.
# Purpose: Reduces overall noise and smooths the image, useful for basic noise reduction.
# Advantages: Simple and effective at reducing random noise.
# Disadvantages: Blurs edges and details, as it smooths across all pixel intensities.
mean_filtered = cv2.blur(image, (5, 5))  # Applying a 5x5 mean filter
## Parameters:
# image: The input image (in grayscale or color) on which the filter is applied.
# (5, 5): This is the size of the kernel or window. It’s a tuple where the first number is the height (rows) and the second is the width (columns) of the kernel. In this case, it's a 5x5 kernel.
# Smaller kernel (e.g., 3x3): The filter is less aggressive in averaging nearby pixels, preserving more detail but possibly less effective at noise reduction.
# Larger kernel (e.g., 7x7, 9x9): The filter becomes more aggressive, averaging over a larger area, thus smoothing the image more but potentially losing more detail.
# -------------------------------------------------------------------------------------------------------------
# 2. Median Filter
# -------------------------------------------------------------------------------------------------------------
# The Median Filter reduces noise by replacing each pixel with the median value within the kernel.
# Unlike the mean filter, it is particularly effective for removing salt-and-pepper noise (sudden black/white pixels).
# Purpose: Preserves edges better than the mean filter and removes isolated outliers in intensity.
# Advantages: Retains edges while removing noise, effective for salt-and-pepper noise.
# Disadvantages: More computationally expensive than mean filter, may not work well for Gaussian noise.
median_filtered = cv2.medianBlur(image, 5)  # Applying a 5x5 median filter
## Parameters:
# image: The input image (grayscale or color) to apply the filter on.
# 5: This is the size of the kernel, specifically the side length of a square. The kernel is typically an odd number (3, 5, 7, etc.) to have a center pixel.
# Smaller kernel (e.g., 3): Effectively removes small noise like salt and pepper noise but might not handle large noise well.
# Larger kernel (e.g., 7, 9): Better for removing larger noise but may blur edges or detail more significantly.
# -------------------------------------------------------------------------------------------------------------
# 3. Gaussian Filter
# -------------------------------------------------------------------------------------------------------------
# The Gaussian Filter smooths the image by averaging pixel values, but it applies a Gaussian weight based on pixel distance.
# Pixels closer to the center of the kernel have a higher weight than those further away, creating a natural blurring effect.
# Purpose: Reduces high-frequency noise and is effective for Gaussian-distributed noise.
# Advantages: Smooths noise without harsh edges, resulting in a natural blur, effective for small, random noise.
# Disadvantages: Still causes some edge blurring, less effective for large noise patterns or structured noise.
gaussian_filtered = cv2.GaussianBlur(image, (5,5), sigmaX=1)  # Applying a 5x5 Gaussian filter with sigma 1
## Parameters:
# image: The input image.
# (5, 5): This is the size of the kernel (height and width). It defines the window over which the Gaussian blur is calculated.
# The kernel size should typically be an odd number. Larger kernel sizes will blur the image more, affecting larger regions.
# sigmaX=1: The standard deviation (σ) for the Gaussian function along the X-axis (horizontal direction).
# Larger σ: Blurs the image more and affects larger areas, making the result smoother.
# Smaller σ: Results in less blur, keeping more of the original details.
# If sigmaY is not set, it will be the same as sigmaX, but you can specify it separately for horizontal vs vertical blurring.
# -------------------------------------------------------------------------------------------------------------
# 4. Bilateral Filter
# -------------------------------------------------------------------------------------------------------------
# The Bilateral Filter smooths the image while preserving edges by considering both spatial distance and intensity difference.
# Unlike Gaussian or mean filters, it assigns higher weights to pixels with similar intensity to the center pixel, preserving edges.
# Purpose: Removes noise and smooths textures, ideal for images with strong edges.
# Advantages: Excellent edge preservation, reduces noise without blurring edges, useful in applications like portrait editing.
# Disadvantages: Computationally intensive, requires tuning parameters, may not handle all noise types as effectively.
bilateral_filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)  # Applying bilateral filter
## Parameters:
# image: The input image.
# d=9: The diameter of the pixel neighborhood used during filtering. This is a spatial parameter that controls how large the surrounding region of each pixel is considered during the blur. A smaller d results in less smoothing.
# Smaller d: More localized smoothing.
# Larger d: Affects a larger neighborhood and thus gives a stronger blur.
# sigmaColor=75: This parameter controls how much the filter smooths pixels based on color similarity. The higher this value, the more similar colors will be mixed.
# Larger sigmaColor: The filter will consider pixels with more different colors as similar and will blur them more.
# sigmaSpace=75: This controls how much spatial distance between pixels affects the smoothing. A larger value means the filter will smooth over larger areas.
# Larger sigmaSpace: Smooths a larger area spatially, keeping more of the detail.
# -------------------------------------------------------------------------------------------------------------
# Display Results
# -------------------------------------------------------------------------------------------------------------
# Using Matplotlib to display the original and filtered images
plt.figure()

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(mean_filtered, cmap='gray')
plt.title('Mean Filtered')

plt.subplot(2, 3, 3)
plt.imshow(median_filtered, cmap='gray')
plt.title('Median Filtered')

plt.subplot(2, 3, 4)
plt.imshow(gaussian_filtered, cmap='gray')
plt.title('Gaussian Filtered')

plt.subplot(2, 3, 5)
plt.imshow(bilateral_filtered, cmap='gray')
plt.title('Bilateral Filtered')

plt.tight_layout()  #automatically adjusts subplot params so that the subplot(s) fits in to the figure area
plt.show()



#-------------------------------------------------------------------------------------------------------------
### Summary of Filters
#-------------------------------------------------------------------------------------------------------------
## Mean Filter:
# Function: Averages pixel values in the window, resulting in an overall smoothing.
# Best For: Simple noise reduction when details and edges are not critical.
# Pros: Easy to apply, fast.
# Cons: Blurs edges, loses detail.

# فیلتر میانگین:
# کاربرد: کاهش نویزهای ساده، زمانی که دقت در لبه‌ها مهم نیست.
# مزایا: سریع و ساده.
# معایب: از دست دادن جزئیات و مات‌شدن تصویر.

#-------------------------------------------------------------------------------------------------------------

## Median Filter:
# Function: Replaces each pixel with the median of the surrounding pixels, preserving edges better.
# Best For: Salt-and-pepper noise, where outliers are isolated.
# Pros: Maintains edges.
# Cons: Computationally more intensive than mean filter.

# فیلتر میانه:
# کاربرد: حذف نویز نمک و فلفلی، حفظ نسبی لبه‌ها.
# مزایا: حفظ لبه‌ها.
# معایب: زمان‌بر.
#--------------------------------------------------------------------------------------------------------------

## Gaussian Filter:
# Function: Averages pixels with a Gaussian weight, smoothing the image naturally without harsh edges.
# Best For: Random, small-scale noise with Gaussian distribution.
# Pros: Natural blur, less edge loss than mean filter.
# Cons: Still causes some edge loss, less effective for large or structured noise.

# فیلتر گاوسی:
# کاربرد: کاهش نویز تصادفی کوچک.
# مزایا: مات‌شدگی طبیعی و صاف.
# معایب: از دست دادن مقداری از جزئیات و لبه‌ها.

#---------------------------------------------------------------------------------------------------------------

## Bilateral Filter:
# Function: Smooths the image while preserving edges by considering both pixel proximity and intensity similarity.
# Best For: Reducing noise while retaining fine edges, useful for faces, natural scenes.
# Pros: Preserves edges, smooths textures.
# Cons: Slow, requires parameter tuning.

# فیلتر دوطرفه:
# کاربرد: کاهش نویز همراه با حفظ لبه‌ها.
# مزایا: حفظ لبه‌ها و بافت‌ها.
# معایب: نیاز به تنظیم دقیق، پردازش سنگین.