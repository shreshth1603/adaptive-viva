from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from backend.database.models import Base
from backend.config import DATABASE_URL
import os

os.makedirs("./data", exist_ok=True)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()