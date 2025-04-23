import cv2
import numpy as np

# Part 1: Read a digital image (color)
image = cv2.imread('image.jpg')

# Part 2: Get the number of rows, columns, and total pixels (size and shape)
rows, cols, channels = image.shape
print(f"Rows: {rows}, Columns: {cols}, Channels: {channels}")
print(f"Total pixels: {rows * cols}")

# Part 3: Show color and grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Color Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Part 4: Get a part of the image
# For example, cropping a region (start_row:end_row, start_col:end_col)
cropped_image = image[50:200, 100:300]  # You can adjust these values
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Part 5: Make some part of the image black or white
# Making the region (50:150, 50:150) black
image[50:150, 50:150] = [0, 0, 0]  # Black color in BGR format

# Making the region (200:300, 200:300) white
image[200:300, 200:300] = [255, 255, 255]  # White color in BGR format

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
