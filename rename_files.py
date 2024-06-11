import os

def rename_files_in_folders(main_folder, file_extension):
    # Walk through all subdirectories in the main folder
    for root, dirs, files in os.walk(main_folder):
        folder_name = os.path.basename(root)
        files_to_rename = [file for file in files if file.lower().endswith(file_extension.lower())]
        
        for index, file in enumerate(files_to_rename, start=1):
            old_file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1]
            new_file_name = f"{folder_name}-{index}{file_ext}"
            new_file_path = os.path.join(root, new_file_name)
            
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} to {new_file_path}')

if __name__ == "__main__":
    main_directory = input("Enter the main directory path: ")
    extension = input("Enter the file extension to rename (e.g., .jpg, .png): ")
    rename_files_in_folders(main_directory, extension)
    print("Renaming completed.")
