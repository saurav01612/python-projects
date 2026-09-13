import cv2
import numpy as np

img = cv2.imread("input.jpg")

# Tested with smaller kernels; final output uses the larger 7x7 kernel.
kernel_small = np.ones((3, 3), np.float32) / 9
result_small = cv2.filter2D(img, -1, kernel_small)

kernel_large = np.ones((7, 7), np.float32) / 49
result_large = cv2.filter2D(img, -1, kernel_large)

cv2.imwrite("output.png", result_large)
