# Task CLI

Terminalden çalışan basit bir görev (task) yöneticisi. Görevleri bir JSON
dosyasında saklar. M1 (Python temelleri) modülünün örnek projesi.

## Özellikler
- Görev ekleme, listeleme, tamamlama, silme (CRUD)
- Önceliğe göre etiketleme (low / medium / high)
- Özet istatistik (toplam / tamamlanan / kalan)
- Veriler `tasks.json` dosyasında kalıcı olarak saklanır

## Mimari
Üç katmanlı yapı:
- `src/models.py` — Task veri modeli
- `src/storage.py` — JSON okuma/yazma (kalıcılık katmanı)
- `src/main.py` — komut satırı arayüzü (controller)

## Kurulum
\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
\`\`\`
Uygulama yalnızca standart kütüphaneyi kullanır; ek paket gerekmez.
Geliştirme araçları için: \`pip install -r requirements-dev.txt\`

## Kullanım
\`\`\`bash
python -m src.main add "Backend çalış" --priority high
python -m src.main list
python -m src.main done 1
python -m src.main remove 2
python -m src.main stats
\`\`\`