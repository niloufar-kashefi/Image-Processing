# Import necessary libraries
import cv2   # OpenCV for image processing
import numpy as np   # Numpy for numerical operations

# Step 1: Create a blank image (white background)
# Create a 512x512 white image with 3 color channels (BGR)
image = np.ones((512, 512, 3), dtype=np.uint8) * 255

# Step 2: Draw a line on the image
# cv2.line(image, start_point, end_point, color, thickness)
cv2.line(image, (50, 50), (400, 50), (255, 0, 0), 5)  # Blue line from (50, 50) to (400, 50), 5 pixels thick

# Step 3: Draw a rectangle on the image
# cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness)
cv2.rectangle(image, (100, 100), (300, 250), (0, 255, 0), 3)  # Green rectangle, 3 pixels thick

# Step 4: Draw a filled rectangle
# cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness)
cv2.rectangle(image, (350, 100), (500, 250), (0, 0, 255), -1)  # Red filled rectangle (thickness = -1)

# Step 5: Draw a circle
# cv2.circle(image, center, radius, color, thickness)
cv2.circle(image, (200, 400), 50, (0, 255, 255), 2)  # Yellow circle, 2 pixels thick

# Step 6: Draw a filled circle
# cv2.circle(image, center, radius, color, thickness)
cv2.circle(image, (400, 400), 75, (255, 0, 255), -1)  # Magenta filled circle (thickness = -1)

# Step 7: Draw an ellipse
# cv2.ellipse(image, center, axes (length,width), angle, start_angle, end_angle, color, thickness)
cv2.ellipse(image, (256, 256), (100, 50), 45, 0, 360, (0, 255, 0), 2)  # Green ellipse rotated by 45 degrees

# Step 8: Draw a polygon
# cv2.polylines(image, [pts], isClosed, color, thickness)
pts = np.array([[50, 300], [100, 350], [50, 400], [100, 450], [50, 500]])
cv2.polylines(image, [pts], isClosed=False, color=(0, 0, 255), thickness=2)  # Red open polygon

# Step 9: Draw an arrow
# cv2.arrowedLine(image, start_point, end_point, color, thickness, tipLength)
cv2.arrowedLine(image, (100, 50), (400, 100), (255, 0, 255), 20, tipLength=0.1)  # Magenta arrow

# Step 10: Add text
# cv2.putText(image, text, org, fontFace, fontScale, color, thickness)
cv2.putText(image, "Hello, OpenCV!", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Step 11: Save the image with shapes
# cv2.imwrite(filename, image)
cv2.imwrite('output_shapes.jpg', image)  # Save the image to a file

# Step 12: Display the result image
# cv2.imshow(window_name, image)
cv2.imshow('Geometric Shapes with Text', image)  # Display the image in a window
cv2.waitKey(0)  # Wait for any key press to close the window
cv2.destroyAllWindows()  # Close all windows




#Tutorial---------------------------------------------------------------------

# Function Syntax and Explanations:

# cv2.line(image, start_point, end_point, color, thickness):
# Draws a line from start_point to end_point.
# Parameters:
#   image: The target image.
#   start_point: Coordinates of the start point (x1, y1).
#   end_point: Coordinates of the end point (x2, y2).
#   color: Color of the line in BGR format (e.g., (255, 0, 0) for blue).
#   thickness: Thickness of the line (in pixels).


# cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness):
# Draws a rectangle between the top-left and bottom-right corners.
# Parameters:
#   top_left_corner: Coordinates of the top-left corner (x1, y1).
#   bottom_right_corner: Coordinates of the bottom-right corner (x2, y2).
#   color: Color of the rectangle (e.g., (0, 255, 0) for green).
#   thickness: Border thickness. Use -1 for a filled rectangle.


# cv2.circle(image, center, radius, color, thickness):
# Draws a circle centered at center with the specified radius.
# Parameters:
#   center: Center of the circle (x, y).
#   radius: Radius of the circle.
#   color: Color of the circle (e.g., (0, 255, 255) for yellow).
#   thickness: Border thickness. Use -1 for a filled circle.


# cv2.ellipse(image, center, axes, angle, start_angle, end_angle, color, thickness):
# Draws an ellipse rotated by angle.
# Parameters:
#   center: Center of the ellipse (x, y).
#   axes: Lengths of the major and minor axes (major_axis, minor_axis).
#   angle: Rotation angle of the ellipse in degrees.
#   start_angle: Starting angle of the elliptic arc (in degrees).
#   end_angle: Ending angle of the elliptic arc (in degrees).
#   color: Color of the ellipse (e.g., (0, 255, 0) for green).
#   thickness: Border thickness. Use -1 for a filled ellipse.


# cv2.polylines(image, [pts], isClosed, color, thickness):
# Draws a polygon with the specified points.
# Parameters:
#   image: The target image.
#   pts: An array of points defining the vertices of the polygon.
#   isClosed: If True, closes the polygon; otherwise, it remains open.
#   color: Color of the polygon (e.g., (0, 0, 255) for red).
#   thickness: Thickness of the lines forming the polygon.


# cv2.arrowedLine(image, start_point, end_point, color, thickness, tipLength):
# Draws an arrowed line from start_point to end_point.
# Parameters:
# image: The target image.
# start_point: Coordinates of the starting point.
# end_point: Coordinates of the ending point.
# color: Color of the arrow (e.g., (255, 0, 255) for magenta).
# thickness: Thickness of the arrow.
# tipLength: Relative length of the arrow tip (default is 0.1).
# cv2.putText(image, text, org, fontFace, fontScale, color, thickness):

# Puts text on the image.
# Parameters:
# image: The target image.
# text: The text string to display.
# org: Bottom-left corner of the text (starting point).
# fontFace: Font type (e.g., cv2.FONT_HERSHEY_SIMPLEX).
# fontScale: Scale factor for the text size.
# color: Color of the text (e.g., (0, 0, 0) for black).
# thickness: Thickness of the text.
# cv2.imwrite(filename, image):

# Saves the image to a file.
# Parameters:
# filename: The name of the file.
# image: The image to be saved.
# cv2.imshow(window_name, image):

# Displays the image in a window.
# Parameters:
# window_name: The name of the window.
# image: The image to be displayed.