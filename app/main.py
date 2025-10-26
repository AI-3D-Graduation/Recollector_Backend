from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import generation
from fastapi.middleware.cors import CORSMiddleware
import os

origins = [
    "http://localhost:3000",
    "https://recollector-frontend.vercel.app"
]
app = FastAPI(title="AI 3D Model Generator")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,    
    allow_methods=["*"],    
    allow_headers=["*"],     
)
app.include_router(generation.router, prefix="/api", tags=["AI Model"])

static_dir = os.path.abspath("static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_root():
    return {"message": "AI 3D Model Generator API is running."}