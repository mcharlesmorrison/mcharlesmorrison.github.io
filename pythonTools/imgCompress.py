import os
from PIL import Image


def compress_images(directory=None, quality=60):
    directory = "/Users/mattmorrison/Desktop/" + directory
    if directory is None:
        directory = os.getcwd()

    # Calculate total size before compression
    total_size_before = sum(
        os.path.getsize(os.path.join(directory, f))
        for f in os.listdir(directory)
        if f.casefold().endswith(".jpg") or f.casefold().endswith(".jpeg")
    )

    for filename in os.listdir(directory):
        if filename.casefold().endswith(".jpg") or filename.casefold().endswith(
            ".jpeg"
        ):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as im:
                im.save(filepath, optimize=True, quality=quality)

    # Calculate total size after compression
    total_size_after = sum(
        os.path.getsize(os.path.join(directory, f))
        for f in os.listdir(directory)
        if f.casefold().endswith(".jpg") or f.casefold().endswith(".jpeg")
    )

    # Convert sizes to megabytes
    total_size_before_mb = total_size_before / (1024 * 1024)
    total_size_after_mb = total_size_after / (1024 * 1024)

    print(f"Total size before compression: {total_size_before_mb:.2f} MB")
    print(f"Total size after compression: {total_size_after_mb:.2f} MB")

    return True  # Return True if no images were found in the directory


def main():
    print(compress_images("bart_fkt"))


if __name__ == "__main__":
    main()
