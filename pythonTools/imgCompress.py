from PIL import Image
import os

directory = "/Users/mattmorrison/Documents/repos/mcharlesmorrison.github.io/image/trt"

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        filepath = os.path.join(directory, filename)
        with Image.open(filepath) as img:
            img.save(filepath, optimize=True, quality=85)