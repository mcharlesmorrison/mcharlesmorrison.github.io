import os
from PIL import Image


def compress_images(directory=None, quality=70):
    directory = "/Users/mattmorrison/Desktop/" + directory
    if directory is None:
        directory = os.getcwd()
    for filename in os.listdir(directory):
        if filename.casefold().endswith(".jpg") or filename.casefold().endswith(
            ".jpeg"
        ):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as im:
                im.save(filepath, optimize=True, quality=quality)
                # # Check if the file size decreased after compression
                # if os.path.getsize(filepath) < os.path.getsize(filepath[:-4] + '_original.jpg'):
                #     os.remove(filepath[:-4] + '_original.jpg')
                #     return True
                # else:
                #     os.remove(filepath)
                #     return False
    return True  # Return True if no images were found in the directory


print(compress_images("panamintTraverse"))
