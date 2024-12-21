import cv2

# خواندن تصویر
image = cv2.imread('image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# لبه‌گیری با Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# پیدا کردن کانتورها
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# رسم کانتورها روی تصویر اصلی
output_image = image.copy()
cv2.drawContours(output_image, contours, -1, (0, 255, 0), 2)

# نمایش تصویر
cv2.imshow('Contours', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
