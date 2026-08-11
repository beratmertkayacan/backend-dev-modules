# Task API (M4)

task-cli'ın (M1) HTTP/REST versiyonu. Görevleri bir API üzerinden yönetir.
FastAPI ile yazıldı. Veriler şu an bellekte tutulur (M5'te PostgreSQL gelecek).

## Çalıştırma

bash
pip install -r requirements.txt
uvicorn main:app --reload

Interaktif dökümantasyon: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoint'ler


| Metot  | Yol         | İş                    |
| ------ | ----------- | --------------------- |
| GET    | /tasks      | Tüm görevleri listele |
| POST   | /tasks      | Yeni görev oluştur    |
| GET    | /tasks/{id} | Tek görev getir       |
| PATCH  | /tasks/{id} | Tamamlandı işaretle   |
| DELETE | /tasks/{id} | Görevi sil            |


örnek sorular: 
• Yeni özellik: "Kullanıcı favori ürünlerini görebilsin" → yeni GET /favorites yaz.
• Var olanı değiştirme: "Ürüne 'indirim' alanı ekle" → modeli + endpoint'i güncelle.
• Bug: "Sipariş listesi yanlış sıralanıyor / hata veriyor" → sebebini bulup düzelt.
• Entegrasyon: "Ödeme için Stripe'ı bağla" → Stripe API'sine istek atan kodu yaz.
• Performans: "Bu endpoint yavaş" → veritabanı sorgusunu optimize et.