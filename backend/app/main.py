from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine
from .routers import user, auth
from dotenv import load_dotenv
load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:5173",
    "https://localhost:3000",
    "http://localhost:3000",
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "https://swadeshfood.com",
    "https://www.swadeshfood.com",
    "http://swadeshfood.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)