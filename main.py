# import os
# import magic

# os.chdir(r"D:\blahh")
# i = 0


# lst = os.listdir(r"D:\blahh")
# length = len(lst)
# mime = magic.Magic(mime=True)
# print(lst[i])


# for i in range(0,length):

#     file_type = mime.from_file(lst[i])


#     if file_type == 'text/plain':
#         if os.path.isdir('text_files') == True:
#             os.rename(lst[i],f"text_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('text_files')
#             os.rename(lst[i],f"text_files/{lst[i]}")

#     elif file_type == 'image/png':
#         if os.path.isdir('PNG_files') == True:
#             os.rename(lst[i], f"PNG_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('PNG_files')
#             os.rename(lst[i], f"PNG_files/{lst[i]}")
        
    
#     elif file_type == 'image/jpeg':
#         if os.path.isdir('JPEG_files') == True:
#             os.rename(lst[i], f"JPEG_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('JPEG_files')
#             os.rename(lst[i], f"JPEG_files/{lst[i]}")

#     elif file_type == 'application/pdf':
#         if os.path.isdir('PDF_files') == True:
#             os.rename(lst[i], f"PDF_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('PDF_files')
#             os.rename(lst[i], f"PDF_files/{lst[i]}")
    
#     elif file_type == 'audio/mpeg':
#         if os.path.isdir('MP3_files') == True:
#             os.rename(lst[i], f"MP3_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('MP3_files')
#             os.rename(lst[i], f"MP3_files/{lst[i]}")

#     elif file_type == 'text/html':
#         if os.path.isdir('HTML_files') == True:
#             os.rename(lst[i], f"HTML_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('HTML_files')
#             os.rename(lst[i], f"HTML_files/{lst[i]}")

#     elif file_type == 'video/mp4':
#         if os.path.isdir('MP4_files') == True:
#             os.rename(lst[i], f"MP4_files/{lst[i]}")
#             continue
#         else:
#             os.mkdir('MP4_files')
#             os.rename(lst[i], f"MP4_files/{lst[i]}")

#     elif file_type == None:
#         continue

import os
import magic

# Define base path
base_path = r"D:\blahh"
os.chdir(base_path)

# Create MIME-type to folder mapping
mime_folder_map = {
    "text/plain": "text_files",
    "image/png": "PNG_files",
    "image/jpeg": "JPEG_files",
    "application/pdf": "PDF_files",
    "audio/mpeg": "MP3_files",
    "text/html": "HTML_files",
    "video/mp4": "MP4_files"
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

    












#while True:

    


# mime = magic.from_file("image.png", mime=True)
# print(mime)  # e.g. "image/jpeg"
