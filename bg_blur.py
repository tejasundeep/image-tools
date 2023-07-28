from rembg import remove
from PIL import Image, ImageFilter

input_path = "input.png"
output_path = "output.png"

input_image = Image.open(input_path)
transparent_image = remove(input_image)

blurred_image = input_image.filter(ImageFilter.GaussianBlur(radius=5))

blurred_image.paste(transparent_image, (0, 0), transparent_image)
blurred_image.save(output_path, quality=100)