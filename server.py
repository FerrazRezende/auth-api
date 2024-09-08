"""
Created by: Matheus Ferraz
AuthAPI
"""


from router.person_router import person_router
from router.session_router import session_router
from router.auth_router import auth_router
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from fastapi import FastAPI
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

# Root route
@app.get("/", tags=["Root"])
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}

# -------------- Server start --------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)