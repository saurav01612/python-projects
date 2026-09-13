import cv2

img = cv2.imread("input.jpg")

# 5x5 is an odd-sized kernel that gives effective smoothing while retaining
# more detail than a very large Gaussian kernel.
result = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite("output.png", result)
