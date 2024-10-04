"""
Created by: Matheus Ferraz
AuthAPI
"""

from middleware.request_logger import RequestLoggerMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from router.session_router import session_router
from router.person_router import person_router
from fastapi.staticfiles import StaticFiles
from router.auth_router import auth_router
from security import JWT_SECRET_KEY
from settings import UPLOAD_DIR
from fastapi import FastAPI
from typing import Dict
import uvicorn
import os




# Server instance
app = FastAPI(
    title="AuthAPI",
    version="0.0.0",
    description="Authentication API that returns a JWT token, stores people and sessions",
)

# |-------------|
# | Middlewares |
# |-------------|
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLoggerMiddleware)
app.add_middleware(SessionMiddleware, secret_key=JWT_SECRET_KEY)

# |--------|
# | Routes |
# |--------|
app.include_router(person_router, prefix="/person", tags=["Person"])
app.include_router(session_router, prefix="/session", tags=["Session"])
app.include_router(auth_router, prefix='/auth', tags=["Auth"])

app.mount("/static", StaticFiles(directory="static"), name="static")

# |------------|
# | Prometheus |
# |------------|
Instrumentator().instrument(app).expose(app)


# Root route
@app.get("/", tags=["Root"])
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}

# -------------- Server start --------------
if __name__ == "__main__":
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    uvicorn.run(app, host="0.0.0.0", port=8000)