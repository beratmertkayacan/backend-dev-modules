# Veritabanı ve ORM (Modül 04)

SQLAlchemy 2.0 ile SQLite üzerinde çalışan bir e-ticaret şeması. Bir müşterinin birden fazla siparişi olabilir (bire çok ilişki). Amaç, ham SQL ile yazılan sorguların ORM karşılığını görmek ve ilişkileri nesne olarak yönetmek.

## Şema

```
customers (1) ───< orders (N)
```

| Tablo | Alanlar |
|---|---|
| `customers` | `id` (PK), `name`, `email` (benzersiz) |
| `orders` | `id` (PK), `product_name`, `price`, `order_date` (varsayılan: şimdi), `customer_id` (FK) |

## Dosyalar

| Dosya | Görev |
|---|---|
| `database.py` | Engine, `SessionLocal` ve ORM taban sınıfı (`Base`). Veritabanı dosyası her zaman bu klasördeki `shop.db` olur |
| `models.py` | `Customer` ve `Order` modelleri, çift yönlü `relationship` tanımları |
| `play.py` | Tabloları sıfırlar ve kurgusal 3 müşteri ile 9 sipariş ekler |
| `exercise.py` | SQL sorgularının ORM karşılıkları |

## Çalıştırma

Komutlar `04-veritabani-orm` klasöründen çalıştırılmalıdır.

```bash
cd 04-veritabani-orm
pip install -r requirements.txt
python play.py       # DİKKAT: mevcut tabloları siler ve yeniden oluşturur
python exercise.py
```

`shop.db` dosyası depoya eklenmez, `play.py` çalıştırılınca yeniden üretilir.

## Sorgu karşılıkları

| SQL | ORM |
|---|---|
| `SELECT * FROM customers` | `db.query(Customer).all()` |
| `WHERE price > 1000` | `db.query(Order).filter(Order.price > 1000)` |
| `ORDER BY price DESC` | `db.query(Order).order_by(Order.price.desc())` |
| `SELECT COUNT(*) FROM orders` | `db.query(Order).count()` |
| `JOIN ... GROUP BY ... SUM(price)` | `db.query(Customer.name, func.sum(Order.price)).join(Order).group_by(Customer.id)` |

Örnek çıktının bir bölümü:

```
Toplam sipariş sayısı: 9
Her müşterinin toplam sipariş fiyatı:
  Ayşe Demir : 68750.0
  Mehmet Kaya : 103400.0
  Zeynep Arslan : 139000.0
```

## Sınırlılıklar

* Yalnızca ekleme (CREATE) ve okuma (READ) uygulandı, ORM ile UPDATE ve DELETE sıradaki adım.
* Şema değişiklikleri için migrasyon aracı yok, `play.py` tabloları baştan oluşturuyor.
* Task API (Modül 03) henüz bu veritabanına bağlı değil.
