import os
import shutil

def move_files_back_to_folders(src_dir, dst_dir, file_extension):
    # Walk through the source directory
    for file in os.listdir(src_dir):
        if file.lower().endswith(file_extension.lower()):
            # Extract the original folder name from the filename
            original_folder_name = file.split('-')[0]
            src_file_path = os.path.join(src_dir, file)
            dst_folder_path = os.path.join(dst_dir, original_folder_name)
            
            # Ensure the destination folder exists
            if not os.path.exists(dst_folder_path):
                os.makedirs(dst_folder_path)
            
            dst_file_path = os.path.join(dst_folder_path, file)
            shutil.move(src_file_path, dst_file_path)
            print(f'Moved: {src_file_path} to {dst_file_path}')

if __name__ == "__main__":
    src_directory = input("Enter the source directory path (where the files are currently located): ")
    dst_directory = input("Enter the destination directory path (where the files should be moved back to): ")
    extension = input("Enter the file extension to move (e.g., .jpg, .png): ")
    move_files_back_to_folders(src_directory, dst_directory, extension)
    print("Moving completed.")
