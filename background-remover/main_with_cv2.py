from rembg import remove
import os
import cv2
import numpy as np

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
        img = cv2.imread(new_path, 0)
        img_rem_bg = remove(img)
        cv2.imwrite(os.path.join(NEW_FOLDER_NAME, f"img{count}.png"), img_rem_bg)
        print(f"img{count} saved successfully")
    except FileNotFoundError:
        print("Path is not correct!!")
    count = count + 1

print("Finish")
