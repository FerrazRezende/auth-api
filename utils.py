from settings import UPLOAD_DIR
from fastapi import UploadFile
from pathlib import Path
import os



# Function for create user dir
def ensure_user_directory(username: str) -> str:
    user_dir = os.path.join(UPLOAD_DIR, username)
    Path(user_dir).mkdir(parents=True, exist_ok=True)
    return user_dir

# Function for save img in user dir
def save_image(file: UploadFile, username: str) -> str:
    user_dir = ensure_user_directory(username)

    file_path = os.path.join(user_dir, "profilepic")

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path
