import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
equalized = cv2.equalizeHist(img)

cv2.imwrite("output.png", equalized)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Before Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("After Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()
