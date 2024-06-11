# File Management Scripts

This repository contains two Python scripts designed to manage files within directories. These scripts allow users to copy and rename files of a specific type, dynamically specified by the user.

## Scripts

1. **copy_files.py**: This script copies files with a specified extension from a source directory to a destination directory, preserving the folder structure.
2. **rename_files.py**: This script renames files with a specified extension to match their parent folder name, appending an index to each file.

## Requirements

- Python 3.x

## Usage

### 1. Copy Files Script (`copy_files.py`)

This script copies files with a specified extension from the source directory to the destination directory, preserving the folder structure.

#### How to Run

1. Open Terminal.
2. Navigate to the directory where you saved the `copy_files.py` script.
3. Run the script using Python:

    ```bash
    python3 copy_files.py
    ```

4. Follow the prompts:
    - Enter the source directory path.
    - Enter the destination directory path.
    - Enter the file extension to copy (e.g., `.jpg`, `.png`).

### 2. Rename Files Script (`rename_files.py`)

This script renames files with a specified extension to match their parent folder name, appending an index to each file.

#### How to Run

1. Open Terminal.
2. Navigate to the directory where you saved the `rename_files.py` script.
3. Run the script using Python:

    ```bash
    python3 rename_files.py
    ```

4. Follow the prompts:
    - Enter the main directory path.
    - Enter the file extension to rename (e.g., `.jpg`, `.png`).

## Example

Consider you have the following directory structure:

```
main_folder/
├── folder1/
│   ├── abc1.jpg
│   ├── abc2.jpg
│   └── file.txt
├── folder2/
│   ├── def1.jpg
│   ├── def2.jpg
│   └── image.png
└── folder3/
    ├── ghi1.jpg
    ├── ghi2.jpg
    └── another_file.txt
```


**Running `copy_files.py`** to copy `.jpg` files to `destination_folder` will result in:

```
destination_folder/
├── folder1/
│   ├── abc1.jpg
│   ├── abc2.jpg
├── folder2/
│   ├── def1.jpg
│   ├── def2.jpg
└── folder3/
    ├── ghi1.jpg
    └── ghi2.jpg
```

**Running `rename_files.py`** in `main_folder` for `.jpg` files will result in:

```
main_folder/
├── folder1/
│   ├── folder1-1.jpg
│   ├── folder1-2.jpg
│   └── file.txt
├── folder2/
│   ├── folder2-1.jpg
│   ├── folder2-2.jpg
│   └── image.png
└── folder3/
    ├── folder3-1.jpg
    ├── folder3-2.jpg
    └── another_file.txt
```


## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
