import cv2
import numpy as np

img = cv2.imread("input.jpg")

# Custom sharpening kernel: emphasizes the center pixel and subtracts
# neighboring pixels to enhance edges/details.
kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
], dtype=np.float32)

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imwrite("output.png", sharpened)
