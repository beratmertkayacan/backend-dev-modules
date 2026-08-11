"""Veritabanı oluştur, 'customers' ve 'orders' tablolarını doldur, ilişki oku"""
from sqlalchemy import func
from database import Base, engine, SessionLocal
from models import Customer, Order

# 1-Tabloları oluştur
Base.metadata.create_all(bind = engine)
db = SessionLocal()


# 2-CREATE: bir müşteri ve ona bağlı iki sipariş
musteri1 = Customer(name = "Berat Mert Kayacan", email = "beratmert.kayacan@gmail.com")
musteri1.orders = [
    Order(product_name = "MacBook", price = 56000.0),
    Order(product_name = "Mouse", price = 750.0),
    Order(product_name = "Printer", price = 12000),
]
db.add(musteri1)          # müşteriyi ekle
db.commit()              # siparişler de otomatik eklenir (ilişki sayesinde)
db.refresh(musteri1)
print(f"Müşteri 1 eklendi: {musteri1.id} - {musteri1.name}")

# Customer 2:
musteri2 = Customer(name = "Isıl Daldaban", email = "isildaldaban@gmail.com")
musteri2.orders = [
    Order(product_name = "Keyboard", price = 2000.0),
    Order(product_name = "Monitor", price = 10000.0),
    Order(product_name = "Iphone17", price = 84000.0),
    Order(product_name = "AirPods Pro", price = 7400.0),
]
db.add(musteri2)
db.commit()
db.refresh(musteri2)
print(f"Müşteri 2 eklendi: {musteri2.id} - {musteri2.name}")