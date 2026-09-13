import cv2
import numpy as np

img = cv2.imread("input.jpg")
increase = 50

enhanced = cv2.add(img, np.full(img.shape, increase, dtype=np.uint8))

print("Pixel before:", img[100, 100])
print("Pixel after :", enhanced[100, 100])

cv2.imwrite("output.png", enhanced)
