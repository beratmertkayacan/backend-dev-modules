"""Veritabanı bağlantısı ve session (oturum) kurulumu"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'shop.db'}"  # her zaman M5-database/shop.db

engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})
SessionLocal = sessionmaker(bind = engine, autoflush = False)

class Base(DeclarativeBase): # tüm ORM modellerinin türeyeceği temel sınıf 
    pass 

