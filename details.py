import cv2
import numpy as np

input_image = cv2.imread('input.png', cv2.IMREAD_UNCHANGED)
blurred = cv2.GaussianBlur(input_image, (9, 9), 0)
detail = cv2.subtract(input_image, blurred)
result = cv2.add(input_image, detail)
result = np.clip(result, 0, 255).astype(np.uint8)

cv2.imwrite('details.png', result)