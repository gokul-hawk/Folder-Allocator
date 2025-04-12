import shutil
from tool import classify_file_gemini
import os
BASE_DIR = os.path.expanduser("~/Downloads")
DEST_DIR = os.path.expanduser("~/Organized")

def move_file(filepath):
    filename = os.path.basename(filepath)
    filetype = filename.split('.')[-1].lower()

    try:
        category = classify_file_gemini(filename, filetype)
        target_folder = os.path.join(DEST_DIR, category)
        os.makedirs(target_folder, exist_ok=True)

        target_path = os.path.join(target_folder, filename)
        shutil.move(filepath, target_path)
        print(f"Moved '{filename}' → '{category}'")
    except Exception as e:
        print(f"Error moving '{filename}': {e}")
