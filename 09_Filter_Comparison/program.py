import cv2
import numpy as np

img = cv2.imread("input.jpg")

mean_kernel = np.ones((5, 5), np.float32) / 25
output_mean = cv2.filter2D(img, -1, mean_kernel)

output_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

output_median = cv2.medianBlur(img, 5)

cv2.imwrite("output_mean.png", output_mean)
cv2.imwrite("output_gaussian.png", output_gaussian)
cv2.imwrite("output_median.png", output_median)
