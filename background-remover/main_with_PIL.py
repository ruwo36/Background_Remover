from PIL import Image
from rembg import remove
import os

NEW_FOLDER_NAME = "design_bg_removed"

# Create "design_bg_removed" if not exit
for folder in os.listdir('.'):
    if folder == NEW_FOLDER_NAME:
        print("Folder already exists.")
    else:
        os.mkdir(NEW_FOLDER_NAME)
        print("Done, folder created.")
        break

# get path for filename
path = input("Enter your folder path: ")

count = 0
for filename in os.listdir(path):
    # merge the path with filename
    new_path = os.path.join(path, filename)
    try:
        img = Image.open(new_path)
        img_rem_bg = remove(img)
        img_rem_bg.save(os.path.join(NEW_FOLDER_NAME, f"img{count}.png"))
        print(f"img{count} saved successfully")
    except FileNotFoundError:
        print("Path is not correct!!")
    count = count + 1

print("Finish")
