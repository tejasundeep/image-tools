import cv2
import image_dehazer

input_image = cv2.imread('input.png')
dehazed_image = image_dehazer.remove_haze(input_image)

cv2.imwrite('cv_dehazed.png', dehazed_image)