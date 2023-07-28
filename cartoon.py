import cv2

input_image = cv2.imread("input.png", cv2.IMREAD_UNCHANGED)
img_style = cv2.stylization(input_image, sigma_s=200, sigma_r=0.35)

cv2.imwrite("cartoon.png", img_style)