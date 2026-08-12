from sqlalchemy import func
from database import SessionLocal
from models import Customer, Order

db = SessionLocal()

# ORM ile SQL sorguları

# 1- Tüm müşteriler: (SELECT * FROM customers)
print("Müşteriler:")
for c in db.query(Customer).all():
    print(" ", c.name)

# 2- 1000 tl üstü siparişler: (SELECT * FROM orders WHERE price > 1000)
print("1000 tl üstü siparişler:")
for o in db.query(Order).filter(Order.price > 1000).all():
    print(" ", o.product_name)

# 3- Sipariş fiyatları azalan sırada: (SELECT * FROM orders ORDER BY price DESC)
print("Azalan sipariş fiyatları:")
for o in db.query(Order).order_by(Order.price.desc()).all():
    print(" ", o.product_name,":", o.price)

# 4- Toplam sipariş sayısı: (SELECT COUNT(*) FROM orders)
print("Toplam sipariş sayısı:", db.query(Order).count())

# 5- Her müşterinin toplam sipariş fiyatı: (SELECT customer_id, SUM(price) FROM orders GROUP BY customer_id)
print("Her müşterinin toplam sipariş fiyatı:")
for c in db.query(Customer.name, func.sum(Order.price).label("total_price")).join(Order).group_by(Customer.id).all():
    print(" ", c.name, ":", c.total_price)