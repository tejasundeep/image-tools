import cv2

input_image = cv2.imread("input.png", cv2.IMREAD_UNCHANGED)
blurred = cv2.GaussianBlur(input_image, (7, 7), 0)

cv2.imwrite("desnoised.png", blurred)