import os
import send2trash
from PIL import Image


def detect_image_files():
    image_files = [filename for filename in os.listdir() if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    return image_files

def move_images_to_trash_with_resolution(width, height):
    for filename in os.listdir():
        if not filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            continue  # skip non-image files

        try:
            with Image.open(filename) as image:
                if image.size == (width, height):
                    send2trash.send2trash(filename)
                    print(f"Moved {filename} to trash")
        except OSError:
            pass  # skip unreadable files

if __name__ == '__main__':
    image_files = detect_image_files()
    print("Image files in current directory:")
    for filename in image_files:
        print(filename)

    width = int(input("Enter image width to move to trash: "))
    height = int(input("Enter image height to move to trash: "))
    move_images_to_trash_with_resolution(width, height)
