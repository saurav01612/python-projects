import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

img_float = np.float32(img)

dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)
shifted_dft = np.fft.fftshift(dft)

print("Original image shape:", img.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT shape:", shifted_dft.shape)

# Save a visualization of the shifted DFT.
magnitude = cv2.magnitude(shifted_dft[:, :, 0], shifted_dft[:, :, 1])
magnitude = 20 * np.log(magnitude + 1)
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
magnitude = np.uint8(magnitude)

cv2.imwrite("output.png", magnitude)
