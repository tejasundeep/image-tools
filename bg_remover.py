from rembg import remove
from PIL import Image

input_path = "input.png"
output_path = "bg_removed.png"

input_image = Image.open(input_path)

output_image = remove(input_image)
output_image.save(output_path)