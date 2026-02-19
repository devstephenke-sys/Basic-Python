import os
import shutil
import time

# Define the folder to organize
folder_to_watch = "C:/Users/YourUserName/Downloads"  # Change this to your folder path

# Define file categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"]
}

# Function to organize files
def organize_folder():
    for filename in os.listdir(folder_to_watch):
        file_path = os.path.join(folder_to_watch, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file type
        moved = False
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                dest_folder = os.path.join(folder_to_watch, folder)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved {filename} → {folder}/")
                moved = True
                break

        # If file type is unknown
        if not moved:
            dest_folder = os.path.join(folder_to_watch, "Others")
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"Moved {filename} → Others/")

# Optional: continuously watch folder
def watch_folder(interval=10):
    print(f"Watching folder: {folder_to_watch} (Checking every {interval} seconds)")
    while True:
        organize_folder()
        time.sleep(interval)

# Run the folder watcher
if __name__ == "__main__":
    watch_folder(interval=10)  # checks every 10 seconds
