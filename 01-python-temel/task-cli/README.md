# Task CLI (Modül 01)

Terminalden çalışan basit bir görev yöneticisi. Görevler bir JSON dosyasında saklanır. Python temelleri modülünün örnek projesidir ve sonraki modüllerde HTTP API ve veritabanı katmanlarına taşınan görev yönetimi fikrinin ilk halidir.

## Özellikler

* Görev ekleme, listeleme, tamamlama ve silme (CRUD)
* Öncelik etiketi: `low`, `medium`, `high`
* Tamamlanan görevleri tek komutla temizleme (`clear`)
* Özet istatistik: toplam, tamamlanan, kalan ve önceliğe göre dağılım
* Veriler `tasks.json` dosyasında kalıcı olarak saklanır, dosya ilk kullanımda otomatik oluşur

## Mimari

Üç katmanlı yapı, her dosyanın tek bir sorumluluğu var:

| Dosya | Sorumluluk | Sonraki modüllerdeki karşılığı |
|---|---|---|
| `src/models.py` | Görev veri modeli (`Task` sınıfı) | Pydantic modeli, ORM modeli |
| `src/storage.py` | JSON okuma ve yazma | Veritabanı katmanı (SQLAlchemy) |
| `src/main.py` | Komut satırı arayüzü | API route'ları (FastAPI) |

## Kurulum

```bash
cd 01-python-temel/task-cli
python3 -m venv .venv
source .venv/bin/activate
```

Uygulama yalnızca Python standart kütüphanesini kullanır, ek paket gerekmez.

## Kullanım

Komutlar `task-cli` klasöründen çalıştırılmalıdır.

```bash
python -m src.main add "Backend çalış" --priority high
python -m src.main list
python -m src.main done 1
python -m src.main remove 2
python -m src.main clear
python -m src.main stats
```

Örnek çıktı:

```
Görev eklendi: [yapılmadı] #1 Backend çalış (high)
Toplam: 1 | Tamamlanan: 0 | Kalan: 1
 high: 1
```

## Sınırlılıklar

* Otomatik test yok, komutlar elle denenerek doğrulandı.
* Başlık doğrulaması yok (boş başlık eklenebilir).
* Eşzamanlı kullanımda JSON dosyası için kilitleme yok, bu yüzden tek kullanıcılı kullanım için uygun.
