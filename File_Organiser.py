import os
import shutil

# File Types Definitions
file_types = {
    "audio": (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv"),
    "video": (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", ".mkv", ".avi", ".wmv", ".flv"),
    "image": (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif", ".bmp"),
    "documents": (".pdf", ".docx", ".txt", ".pptx", ".xlsx"),
    "photoshops": (".psd"),
    "compressed": (".zip", ".rar", ".7z"),
    "executable": (".exe", ".msi", ".bat"),
}

# Matching file extension to file type
def is_file_of_type(file, file_type):
    return os.path.splitext(file)[1] in file_types[file_type]

# Organising the files
def organise_file(file_path, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.move(file_path, destination_folder)
    except Exception as e:
        print(f"Error organizing file {file_path}: {e}")

# Destination Folders
# base_folder = os.path.expanduser("~/Downloads")
base_folder = base_folder = os.getcwd()
destination_folders = {file_type: os.path.join(base_folder, file_type) for file_type in file_types}
destination_folders["others"] = os.path.join(base_folder, "others")

# Iterate through files in the specified base folder
for file in os.listdir(base_folder):
    file_path = os.path.join(base_folder, file)

    # Skip directories/files to not organise
    if os.path.isdir(file_path) or file.startswith("."):
        continue

    organised = False
    for file_type, extensions in file_types.items():
        if is_file_of_type(file, file_type):
            organise_file(file_path, destination_folders[file_type])
            organised = True
            break

    if not organised:
        organise_file(file_path, destination_folders["others"])