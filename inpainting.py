import cv2

image = cv2.imread('input.png')
mask = cv2.imread('mask.png', 0)

mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
inpaint = cv2.inpaint(image, mask, 15, cv2.INPAINT_TELEA)

cv2.imwrite("inpainted.png", inpaint)