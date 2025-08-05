
import os
import magic

# Define base path
base_path = input("Enter your folder path: ")

#Raises a custom error when an invalid directory path is given as the input
if not os.path.isdir(base_path)
    raise DirectoryNotFoundError(base_path)

os.chdir(base_path)

# Create MIME-type to folder mapping
mime_folder_map = {
    "text/plain": "text_files",
    "image/png": "PNG_files",
    "image/jpeg": "JPEG_files",
    "application/pdf": "PDF_files",
    "audio/mpeg": "MP3_files",
    "text/html": "HTML_files",
    "video/mp4": "MP4_files",
    "text/csv":  "CSV_files",
    "image/gif": "GIF_files",
    "application/zip": "ZIP_files",
    "application/json": "JSON_files",
    "application/xml": "XML_files"
    
}

# Initialize magic
mime = magic.Magic(mime=True)

# Loop through all items in the directory
for file in os.listdir(base_path):
    full_path = os.path.join(base_path, file)

    # Skip directories
    if os.path.isdir(full_path):
        continue

    try:
        file_type = mime.from_file(full_path)
    except Exception as e:
        print(f"Skipping {file} due to error: {e}")
        continue

    # Check if the MIME type is in our mapping
    if file_type in mime_folder_map:
        target_folder = os.path.join(base_path, mime_folder_map[file_type])

        # Create target folder if it doesn't exist
        os.makedirs(target_folder, exist_ok=True)

        # Move file
        target_path = os.path.join(target_folder, file)
        os.rename(full_path, target_path)
        print(f"Moved {file} to {target_folder}")

    















