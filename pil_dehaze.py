from PIL import Image
import numpy as np
import image_dehazer

input_image = Image.open('input.png')
input_image = np.array(input_image)

dehazed_image = image_dehazer.remove_haze(input_image)
dehazed_image = Image.fromarray(dehazed_image)

dehazed_image.save('dehazed.png')