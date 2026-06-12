from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database.db import init_db

app = FastAPI(
    title="Adaptive Viva Evaluation System",
    description="AI-powered autonomous viva examiner",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "Adaptive Viva System is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}