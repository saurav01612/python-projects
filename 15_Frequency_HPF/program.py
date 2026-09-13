import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(dft)

# Circular high-pass mask: suppress the central low-frequency region.
radius = 30
y, x = np.ogrid[:rows, :cols]
low_region = ((x - ccol) ** 2 + (y - crow) ** 2 <= radius ** 2)
mask_single = (~low_region).astype(np.float32)
mask = cv2.merge([mask_single, mask_single])

filtered = shifted * mask
ishifted = np.fft.ifftshift(filtered)
inverse = cv2.idft(ishifted)
result = cv2.magnitude(inverse[:, :, 0], inverse[:, :, 1])

result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)
result = np.uint8(result)

cv2.imwrite("output.png", result)
