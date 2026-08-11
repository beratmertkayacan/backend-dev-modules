"""Veritabanı bağlantısı ve session (oturum) kurulumu"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./shop.db" # geçici olarak SQLite (PostgreSQL gelecek)

engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})
SessionLocal = sessionmaker(bind = engine, autoflush = False)

class Base(DeclarativeBase): # tüm ORM modellerinin türeyeceği temel sınıf 
    pass 

