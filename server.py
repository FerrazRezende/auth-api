from router.person_router import person_router
from router.session_router import session_router
from router.auth_router import auth_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(person_router, prefix="/person", tags=["Person"])
app.include_router(session_router, prefix="/session", tags=["Session"])
app.include_router(auth_router, prefix='/auth', tags=["Auth"])


@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)