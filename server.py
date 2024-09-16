"""
Created by: Matheus Ferraz
AuthAPI
"""
import os
from pathlib import Path

from typing_extensions import Annotated

from depends import get_current_user
from router.person_router import person_router
from router.session_router import session_router
from router.auth_router import auth_router
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from fastapi import FastAPI, UploadFile, Depends, File, HTTPException
from fastapi.staticfiles import StaticFiles
import uvicorn

# Server instance
app = FastAPI(
    title="AuthAPI",
    version="0.0.0",
    description="Authentication API that returns a JWT token, stores people and sessions",
)

# |--------------|
# | CORS Session |
# |--------------|
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# |--------|
# | Routes |
# |--------|
app.include_router(person_router, prefix="/person", tags=["Person"])
app.include_router(session_router, prefix="/session", tags=["Session"])
app.include_router(auth_router, prefix='/auth', tags=["Auth"])


app.mount("/static", StaticFiles(directory="static"), name="static")



UPLOAD_DIR = "static/img/"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def ensure_user_directory(username: str):
    user_dir = os.path.join(UPLOAD_DIR, username)
    Path(user_dir).mkdir(parents=True, exist_ok=True)
    return user_dir


def save_image(file: UploadFile, username: str) -> str:
    user_dir = ensure_user_directory(username)

    file_path = os.path.join(user_dir, "profilepic")

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path


@app.post("/upload-photo/", tags=["Profile pic"])
async def upload_user_photo(
        file: Annotated[UploadFile, File(description="User profile image")],
        current_user: dict = Depends(get_current_user)
):
    username = current_user.username

    try:
        file_path = save_image(file, username)

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error saving file")

    return {"message": f"File uploaded successfully", "filepath": file_path}


# Root route
@app.get("/", tags=["Root"])
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}

# -------------- Server start --------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)