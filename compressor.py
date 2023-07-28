from PIL import Image

input_image = 'input.png'
output_image = 'output.png'
compression_level = 1

img = Image.open(input_image)
img.save(output_image, optimize=True, compress_level=compression_level)