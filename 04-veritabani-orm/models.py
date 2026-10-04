"""E-commerce veritabanı modelleri: Müşteri (1) -> N Sipariş"""

from datetime import datetime
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    name: Mapped[str] = mapped_column(String, nullable = False)
    email: Mapped[str] = mapped_column(String, nullable = False, unique = True)

    orders: Mapped[list["Order"]] = relationship(back_populates = "customer") # bir müşterinin birden fazla siparişi olabilir(1->N ilişkisi)



class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    product_name: Mapped[str] = mapped_column(String, nullable = False)
    price: Mapped[float] = mapped_column(Float, nullable = False)
    order_date: Mapped[datetime] = mapped_column(DateTime, nullable = False, default = func.now())

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id")) # siparişin hangi müşteriye ait olduğunu belirtir(Foreign Key)
    customer: Mapped["Customer"] = relationship(back_populates = "orders") # bir siparişin bir müşterisi olmalı(N->1 ilişkisi)
