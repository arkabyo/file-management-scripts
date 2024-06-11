import os
import shutil

def copy_files(src_dir, dst_dir, file_extension):
    # Ensure the destination directory exists
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Walk through source directory
    for root, dirs, files in os.walk(src_dir):
        # Check if there are any files with the specified extension in the current directory
        files_to_copy = [file for file in files if file.lower().endswith(file_extension.lower())]
        
        if files_to_copy:
            # Create the corresponding directory in the destination
            rel_path = os.path.relpath(root, src_dir)
            dst_folder_path = os.path.join(dst_dir, rel_path)
            if not os.path.exists(dst_folder_path):
                os.makedirs(dst_folder_path)
            
            # Copy each file
            for file in files_to_copy:
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst_folder_path, file)
                shutil.copy2(src_file_path, dst_file_path)
                print(f'Copied: {src_file_path} to {dst_file_path}')

if __name__ == "__main__":
    src_directory = input("Enter the source directory path: ")
    dst_directory = input("Enter the destination directory path: ")
    extension = input("Enter the file extension to copy (e.g., .jpg, .png): ")
    copy_files(src_directory, dst_directory, extension)
    print("Copying completed.")
