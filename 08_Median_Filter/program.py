import cv2

img = cv2.imread("input.jpg")

result = cv2.medianBlur(img, 5)

cv2.imwrite("output.png", result)
