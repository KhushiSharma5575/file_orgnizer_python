import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            ext = file.split(".")[-1] if "." in file else "others"
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(filepath, folder)
            print(f"Moved: {file} -> {folder}")

def main():
    dir_path = input("Enter the directory to organize: ").strip()
    organize_files(dir_path)

if __name__ == "__main__":
    main()
