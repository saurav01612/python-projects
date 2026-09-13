import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
highest_frequency_intensity = int(np.argmax(hist))

print("Intensity with highest frequency:", highest_frequency_intensity)

plt.figure()
plt.plot(hist)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Image Histogram")
plt.savefig("output.png", bbox_inches="tight")
plt.close()
