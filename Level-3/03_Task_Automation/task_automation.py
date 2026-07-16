# --------------------------------------------
# Project : Task Automation
# Author  : Dakshinya A
# Description:
# Automatically organizes files into folders
# based on their file extensions.
# --------------------------------------------

import os
import shutil

# Folder to organize
folder_path = input("Enter the folder path to organize: ")

if not os.path.exists(folder_path):
    print("The folder does not exist.")
    exit()

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".c", ".cpp"],
    "Archives": [".zip", ".rar"]
}

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        moved = False

        for folder_name, extensions in file_types.items():

            if file.lower().endswith(tuple(extensions)):

                destination = os.path.join(folder_path, folder_name)

                os.makedirs(destination, exist_ok=True)

                shutil.move(file_path, os.path.join(destination, file))

                print(f"Moved: {file} → {folder_name}")

                moved = True
                break

        if not moved:

            others = os.path.join(folder_path, "Others")

            os.makedirs(others, exist_ok=True)

            shutil.move(file_path, os.path.join(others, file))

            print(f"Moved: {file} → Others")

print("\n✅ File organization completed successfully!")