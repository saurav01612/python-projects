import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

min_val = np.min(img)
max_val = np.max(img)

print("Minimum intensity:", min_val)
print("Maximum intensity:", max_val)

if max_val != min_val:
    stretched = ((img.astype(np.float32) - min_val) * 255 /
                 (max_val - min_val)).astype(np.uint8)
else:
    stretched = img.copy()

cv2.imwrite("output.png", stretched)
