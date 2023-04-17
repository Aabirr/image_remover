import os
import send2trash
import tkinter as tk
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox


def detect_image_files(directory):
    image_files = [filename for filename in os.listdir(directory) if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    return image_files


def move_images_to_trash_with_resolution(directory, width, height):
    count_deleted = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if not filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            continue  # skip non-image files

        try:
            with Image.open(filepath) as image:
                if image.size == (width, height):
                    send2trash.send2trash(filepath)
                    count_deleted += 1
                    print(f"Moved {filename} to trash")
        except OSError:
            pass  # skip unreadable files

    if count_deleted > 0:
        messagebox.showinfo("Deleted", f"Deleted {count_deleted} images")


def browse_directory():
    directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, directory)


def on_submit():
    directory = entry_directory.get()
    image_files = detect_image_files(directory)
    listbox.delete(0, tk.END)
    for filename in image_files:
        listbox.insert(tk.END, filename)


def on_delete():
    directory = entry_directory.get()
    width = int(entry_width.get())
    height = int(entry_height.get())
    move_images_to_trash_with_resolution(directory, width, height)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Image Deleter")

    # Create GUI elements
    label_directory = tk.Label(root, text="Directory:")
    entry_directory = tk.Entry(root)
    button_browse = tk.Button(root, text="Browse", command=browse_directory)
    label_width = tk.Label(root, text="Width:")
    entry_width = tk.Entry(root)
    label_height = tk.Label(root, text="Height:")
    entry_height = tk.Entry(root)
    button_submit = tk.Button(root, text="Submit", command=on_submit)
    listbox = tk.Listbox(root, height=10, width=50)
    button_delete = tk.Button(root, text="Delete", command=on_delete)
    button_close = tk.Button(root, text="Close", command=root.quit)

    # Position GUI elements
    label_directory.grid(row=0, column=0, sticky=tk.W)
    entry_directory.grid(row=0, column=1, sticky=tk.W)
    button_browse.grid(row=0, column=2, sticky=tk.W)
    label_width.grid(row=1, column=0, sticky=tk.W)
    entry_width.grid(row=1, column=1, sticky=tk.W)
    label_height.grid(row=2, column=0, sticky=tk.W)
    entry_height.grid(row=2, column=1, sticky=tk.W)
    button_submit.grid(row=3, column=0, sticky=tk.W)
    listbox.grid(row=4, column=0, columnspan=2)
    button_delete.grid(row=5, column=0, sticky=tk.W)
    button_close.grid(row=5, column=1, sticky=tk.E)

    root.mainloop()
