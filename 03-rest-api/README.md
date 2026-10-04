# Task API (Modül 03)

[Modül 01](../01-python-temel/task-cli) içindeki komut satırı görev yöneticisinin HTTP üzerinden kullanılan sürümü. FastAPI ile yazıldı. Veriler şu an bellekte tutulur, sunucu yeniden başlayınca silinir. Veritabanına bağlanması sıradaki adımdır (Modül 05, bkz. ana README'deki yol haritası).

## Çalıştırma

```bash
cd 03-rest-api
pip install -r requirements.txt
uvicorn main:app --reload
```

Etkileşimli dokümantasyon sunucu çalışırken şu adreste açılır: http://127.0.0.1:8000/docs

## Endpoint'ler

| Metot | Yol | İş | Başarılı durum kodu |
|---|---|---|---|
| GET | `/tasks` | Tüm görevleri listeler | 200 |
| POST | `/tasks` | Yeni görev oluşturur | 201 |
| GET | `/tasks/{id}` | Tek görev getirir | 200 |
| PATCH | `/tasks/{id}` | Görevi tamamlandı işaretler | 200 |
| DELETE | `/tasks/{id}` | Görevi siler | 204 |

Var olmayan bir ID için `GET`, `PATCH` ve `DELETE` istekleri `404` ve `{"detail": "Görev bulunamadı"}` döndürür. Geçersiz öncelik değeri (`low`, `medium`, `high` dışında) `422` ile reddedilir.

Örnek istek:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Backend çalış", "priority": "high"}'
```

```json
{"title": "Backend çalış", "priority": "high", "id": 1, "done": false}
```

## Testler

11 testten oluşan `pytest` seti, bütün endpoint'leri ve hata durumlarını kapsar.

```bash
cd 03-rest-api
pip install -r requirements-dev.txt
pytest
```

## Düzeltilen hata

İlk sürümde `HTTPException` içe aktarılmamıştı ve `PATCH` ile `DELETE` fonksiyonlarındaki `raise` satırı döngünün içinde kalmıştı. Bunun sonucu olarak listedeki ilk görev dışında bir görevi tamamlamak ya da silmek, ve var olmayan bir görev istemek `500` hatası veriyordu. Arama mantığı `find_task` yardımcı fonksiyonuna taşındı ve bu durumlar testlerle güvence altına alındı.

## Sınırlılıklar

* Depo bellek içi, kalıcı değil.
* Görev başlığı güncelleme (`PUT`) ve filtreleme yok.
* Kimlik doğrulama yok.
