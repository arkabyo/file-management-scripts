import os
import shutil

def copy_files_to_single_folder(src_dir, dst_dir, file_extension):
    # Ensure the destination directory exists
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Walk through source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(file_extension.lower()):
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst_dir, file)
                shutil.copy2(src_file_path, dst_file_path)
                print(f'Copied: {src_file_path} to {dst_file_path}')

if __name__ == "__main__":
    src_directory = input("Enter the source directory path: ")
    dst_directory = input("Enter the destination directory path: ")
    extension = input("Enter the file extension to copy (e.g., .jpg, .png): ")
    copy_files_to_single_folder(src_directory, dst_directory, extension)
    print("Copying completed.")
