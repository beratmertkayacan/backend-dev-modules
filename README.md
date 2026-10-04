# Backend ve Yapay Zeka Mühendisliği Modülleri

Python ile backend mühendisliğini temelden başlayarak adım adım öğrenmek ve bunu yapay zeka mühendisliğine bağlamak için hazırlanan modüler bir alıştırma ve mini proje serisi. Her modül kendi klasöründe çalışan bir proje, README ve (mümkün olduğunda) testlerle ilerler.

Hedef kapsam: **Python, Temiz Mimari, SQL ve NoSQL veritabanları, REST ve FastAPI, Asenkron programlama, Mikroservisler, Güvenlik, DevOps, Sistem Tasarımı ve bunların üzerine PyTorch, model servisleme, LLM uygulamaları ve MLOps.** Yani bir yapay zeka mühendisi rolünde backend ve veritabanı tarafında bilinmesi gereken şeylerin tek bir yerde sıralı biçimde toplanması. Repo çalışılarak sırayla geliştiriliyor.

**Şu an kullanılanlar:** Python, FastAPI, Pydantic, SQLAlchemy 2.0, SQLite, httpx, pytest, Git

## İçindekiler

1. [Modüllerin Durumu](#modüllerin-durumu)
2. [Tamamlanan ve Devam Eden Modüller](#tamamlanan-ve-devam-eden-modüller)
3. [Sıradaki Adımlar](#sıradaki-adımlar)
4. [Planlanan Modüller](#planlanan-modüller)
5. [Mimarinin Evrimi](#mimarinin-evrimi)
6. [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
7. [Klasör Yapısı ve Düzen Kuralları](#klasör-yapısı-ve-düzen-kuralları)
8. [Bilinen Eksikler](#bilinen-eksikler)
9. [Geliştirme Geçmişi](#geliştirme-geçmişi)



## Modüllerin Durumu

Modüller 01'den 19'a kadar kesintisiz numaralandırıldı ve üç bölüme ayrıldı. Her bölüm bir öncekinin üzerine kurulur.

### Bölüm 1: Temel


| No  | Modül                                                 | Durum                         | Klasör                                 |
| --- | ----------------------------------------------------- | ----------------------------- | -------------------------------------- |
| 01  | Python temelleri, katmanlı mimari, JSON ile kalıcılık | Tamamlandı                    | [01-python-temel](01-python-temel)     |
| 02  | HTTP istek ve cevap döngüsü, metotlar, durum kodları  | Tamamlandı                    | [02-http](02-http)                     |
| 03  | FastAPI ile REST API ve CRUD                          | Tamamlandı (veriler bellekte) | [03-rest-api](03-rest-api)             |
| 04  | SQLAlchemy ORM, ilişkili tablolar, ORM sorguları      | Devam ediyor                  | [04-veritabani-orm](04-veritabani-orm) |




### Bölüm 2: Backend Mühendisliği


| No  | Modül                            | Durum     | Klasör                   |
| --- | -------------------------------- | --------- | ------------------------ |
| 05  | API ve veritabanı entegrasyonu   | Planlandı | `05-api-db-entegrasyonu` |
| 06  | PostgreSQL, ileri SQL ve Alembic | Planlandı | `06-postgresql-alembic`  |
| 07  | NoSQL: MongoDB ve Redis          | Planlandı | `07-nosql`               |
| 08  | Temiz mimari ve test stratejisi  | Planlandı | `08-temiz-mimari`        |
| 09  | Asenkron Python                  | Planlandı | `09-async`               |
| 10  | Güvenlik                         | Planlandı | `10-guvenlik`            |
| 11  | DevOps                           | Planlandı | `11-devops`              |
| 12  | Mikroservisler ve mesajlaşma     | Planlandı | `12-mikroservisler`      |
| 13  | Sistem tasarımı                  | Planlandı | `13-sistem-tasarimi`     |




### Bölüm 3: Yapay Zeka Mühendisliği


| No  | Modül                                               | Durum     | Klasör                 |
| --- | --------------------------------------------------- | --------- | ---------------------- |
| 14  | PyTorch temelleri                                   | Planlandı | `14-pytorch-temelleri` |
| 15  | Model eğitimi ve deney takibi                       | Planlandı | `15-model-egitimi`     |
| 16  | Model servisleme (inference API)                    | Planlandı | `16-model-servisleme`  |
| 17  | LLM uygulamaları: embedding, vektör veritabanı, RAG | Planlandı | `17-llm-rag`           |
| 18  | MLOps: izleme, versiyonlama, otomasyon              | Planlandı | `18-mlops`             |
| 19  | Bitirme projesi: uçtan uca yapay zeka platformu     | Planlandı | `19-bitirme-projesi`   |




## Tamamlanan ve Devam Eden Modüller



### 01: Task CLI

Terminalden görev ekleyen, listeleyen, tamamlayan, silen, temizleyen ve istatistik gösteren bir uygulama. Kod üç katmana ayrıldı: model (`Task`), kalıcılık (`storage.py`, JSON) ve arayüz (`main.py`, argparse). Bu ayrım sonraki modüllerin temelini oluşturuyor: model katmanı Pydantic ve ORM modellerine, kalıcılık katmanı veritabanına, arayüz katmanı API route'larına dönüşüyor. Detaylar [README](01-python-temel/task-cli/README.md) dosyasında.

### 02: HTTP

`httpx` ile herkese açık bir test API'sine (JSONPlaceholder) elle istek atan iki betik. İstek ve cevabın yapısı, `GET` ve `POST` metotları, `200`, `201` ve `404` durum kodları, JSON verinin Python sözlüğüne çevrilmesi (deserialize) incelendi.

### 03: Task API

Modül 01'deki görev yöneticisinin FastAPI ile yazılmış REST sürümü: listeleme, oluşturma, tek kayıt getirme, tamamlama ve silme endpoint'leri. Girdi doğrulaması Pydantic ile yapılıyor (öncelik yalnızca `low`, `medium`, `high`). 11 testle doğrulandı. Detaylar [README](03-rest-api/README.md) dosyasında.

### 04: Veritabanı ve ORM 

Müşteri ve sipariş tabloları arasında bire çok ilişki kuran SQLAlchemy modelleri, örnek veri üretimi ve SQL sorgularının ORM karşılıkları (filtreleme, sıralama, sayma, birleştirme ile gruplama). ORM ile ekleme ve okuma yapıldı, güncelleme ve silme sırada. Detaylar [README](04-veritabani-orm/README.md) dosyasında.

## Sıradaki Adımlar

### Adım 1: Modül 04'ü bitirmek

- ORM ile UPDATE ve DELETE (`db.get`, alan değiştirip `commit`, `db.delete`).
- Sorguları SQLAlchemy 2.0 stiline (`select()`) çevirmek.
- İlişkili kayıtları verimli yüklemek (`selectinload`) ve N+1 sorgu problemini gözlemlemek.
- Bellek içi SQLite ile `pytest` testleri yazmak.
- **Bitti ölçütü:** `exercise.py` içindeki tüm sorgular `select()` ile yazılmış, güncelleme ve silme dahil dört CRUD işlemi testle doğrulanmış.



### Adım 2: Modül 05, API ile veritabanını birleştirmek

- `Task` için SQLAlchemy modeli ve `get_db` bağımlılığı (`Depends`) ile oturum yönetimi.
- Pydantic şemalarını ayırmak: `TaskCreate`, `TaskRead`, `TaskUpdate`.
- `PUT` ile `PATCH` farkı, filtreleme (`?done=true&priority=high`) ve sayfalama (`limit`, `offset`).
- Testlerde bağımlılık değiştirme (`dependency_overrides`) ile test veritabanı kullanmak.
- **Bitti ölçütü:** Sunucu yeniden başlayınca görevler kaybolmuyor, Modül 03'teki 11 test veritabanı ile de geçiyor.



### Adım 3: Modül 06, PostgreSQL ve Alembic

- PostgreSQL'i yerelde çalıştırmak (Docker ile tek komut) ve `psycopg` ile bağlanmak.
- Alembic ile migrasyon oluşturmak ve geri almak.
- İndeks, transaction ve izolasyon seviyeleri, `EXPLAIN ANALYZE` ile yavaş sorgu analizi.
- **Bitti ölçütü:** Şema yalnızca migrasyonlarla değişiyor, bir sorgu indeks ekleyerek ölçülebilir biçimde hızlanıyor.



### Adım 4: Modül 07, NoSQL

- Redis ile `GET /tasks` için önbellek (cache aside) ve önbellek geçersiz kılma.
- MongoDB'de olay ve log kayıtları için bir koleksiyon.
- SQL ile NoSQL arasında hangi durumda hangisinin seçileceğini anlatan karar tablosu.
- **Bitti ölçütü:** Önbellekli ve önbelleksiz istek süreleri ölçülmüş ve README'ye yazılmış.



### Adım 5: Modül 08, Temiz mimari ve test stratejisi

- Kodu `router`, `service`, `repository` katmanlarına ayırmak ve bağımlılıkları enjekte etmek.
- Alan hataları (domain exception) ve tutarlı hata cevapları.
- Birim, entegrasyon ve uçtan uca test ayrımı, `pytest` fixture'ları ve kapsam (coverage) raporu.
- **Bitti ölçütü:** İş mantığı veritabanı ve HTTP detaylarından bağımsız test edilebiliyor.



## Planlanan Modüller

Bu bölüm kapsamı gösterir. Ayrıntılar modüle gelindiğinde güncellenecek.

### Bölüm 2: Backend Mühendisliği


| No  | Modül           | Başlıca konular                                                                                          | Mini proje                                                         |
| --- | --------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 09  | Asenkron Python | `asyncio`, `async` SQLAlchemy, asenkron `httpx`, arka plan görevleri, kuyruk mantığı                     | Birden fazla dış API'yi paralel çağıran toplayıcı servis           |
| 10  | Güvenlik        | Parola hash'leme, JWT, OAuth2, rol tabanlı yetki, hız sınırlama, CORS, OWASP Top 10                      | Kullanıcıya bağlı görevler ve kimlik doğrulama                     |
| 11  | DevOps          | Docker, `docker compose`, ortam değişkenleri, loglama, GitHub Actions ile CI, dağıtım                    | API ve PostgreSQL'i tek komutla ayağa kaldıran yapı                |
| 12  | Mikroservisler  | Servis sınırları, API gateway, olay tabanlı iletişim, RabbitMQ veya Kafka, servisler arası hata yönetimi | Kullanıcı, görev ve bildirim servislerine bölünmüş uygulama        |
| 13  | Sistem tasarımı | Ölçekleme, yük dengeleme, önbellek stratejileri, veri bölümleme, tutarlılık ve CAP, vaka çalışmaları     | Bir URL kısaltıcı ve bir akış (feed) sistemi için tasarım dokümanı |




### Bölüm 3: Yapay Zeka Mühendisliği


| No  | Modül                         | Başlıca konular                                                                                                              | Mini proje                                         |
| --- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| 14  | PyTorch temelleri             | Tensor, `autograd`, `nn.Module`, kayıp fonksiyonları, optimizer, eğitim döngüsü, GPU kullanımı                               | Sıfırdan yazılmış bir sınıflandırma modeli         |
| 15  | Model eğitimi ve deney takibi | Veri yükleme (`Dataset`, `DataLoader`), doğrulama, aşırı uyum kontrolü, hiperparametre denemeleri, MLflow veya benzeri takip | Tablo verisi üzerinde karşılaştırmalı deney raporu |
| 16  | Model servisleme              | FastAPI ile çıkarım (inference) endpoint'i, model yükleme, toplu istek, ONNX veya TorchScript, model versiyonlama            | Eğitilmiş modeli sunan, testli bir tahmin API'si   |
| 17  | LLM uygulamaları              | Embedding, vektör arama (pgvector veya Qdrant), RAG hattı, araç çağırma, değerlendirme                                       | Kendi dokümanları üzerinde soru cevaplayan servis  |
| 18  | MLOps                         | Veri ve model versiyonlama, model izleme, veri kayması (drift), eğitim hattı otomasyonu, GPU'lu Docker imajı                 | Otomatik yeniden eğitilen ve izlenen model hattı   |
| 19  | Bitirme projesi               | Önceki modüllerin birleşimi: kimlik doğrulama, veritabanı, model servisi, RAG, izleme, CI ve dağıtım                         | Uçtan uca yapay zeka platformu                     |




## Mimarinin Evrimi

Seri boyunca aynı görev yönetimi fikri her modülde bir katman daha kazanıyor:

```
01  CLI uygulaması -> JSON dosyası
03  HTTP API -> bellek içi liste
04  ORM modelleri -> SQLite (API'den bağımsız)
05  HTTP API  ->  ORM -> SQLite
06  HTTP API  ->  ORM -> PostgreSQL + migrasyonlar
07  + Redis önbellek, MongoDB olay kayıtları
08  router -> service -> repository katmanları
10  + kimlik doğrulama ve yetkilendirme
11  + Docker ve CI
12  Mikroservislere bölünme
16  + model servisleme ile yapay zeka endpoint'leri
```

Şu an 04'teki ORM katmanı ile 03'teki API birbirinden ayrı çalışıyor, ikisinin birleşmesi Adım 2'de.

## Kurulum ve Çalıştırma

```bash
git clone git@github.com:beratmertkayacan/backend-dev-modules.git
cd backend-dev-modules
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Her modül kendi klasöründen çalıştırılır:

```bash
# 01: komut satırı görev yöneticisi
cd 01-python-temel/task-cli && python -m src.main list

# 02: HTTP betikleri (internet gerekir)
cd 02-http && python explore.py && python explore2.py

# 03: API ve testler
cd 03-rest-api && uvicorn main:app --reload
cd 03-rest-api && pytest

# 04: veritabanı
cd 04-veritabani-orm && python play.py && python exercise.py
```



## Klasör Yapısı ve Düzen Kuralları

```
.
├── 01-python-temel/
│   └── task-cli/
│       └── src/                models.py, storage.py, main.py
├── 02-http/                    explore.py, explore2.py
├── 03-rest-api/
│   ├── main.py                 FastAPI uygulaması
│   └── tests/                  pytest testleri
├── 04-veritabani-orm/          database.py, models.py, play.py, exercise.py
├── requirements.txt            tüm modüllerin ortak bağımlılıkları
└── README.md
```



## Bilinen Eksikler

- Task API (Modül 03) ile veritabanı (Modül 04) henüz bağlı değil, API verileri bellekte tutuyor ve yeniden başlatmada kayboluyor.
- Veritabanı olarak yalnızca SQLite kullanıldı, PostgreSQL, NoSQL ve migrasyon aracı yok.
- ORM tarafında yalnızca ekleme ve okuma var, güncelleme ve silme uygulanmadı.
- Test kapsamı yalnızca Modül 03 için var, 01 ve 04 için otomatik test yok.
- Kimlik doğrulama, kullanıcı modeli ve yetkilendirme yok.
- Yapılandırma (`.env`), loglama ve merkezi hata yönetimi yok.
- Docker, CI ve dağıtım adımları yok.
- Yapay zeka bölümünün (Modül 14 ve sonrası) henüz hiçbir kodu yok, yalnızca kapsamı ve sırası belirlendi.





