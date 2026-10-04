"""HTTP istek-cevap döngüsünü elle keşfetme."""

import httpx

url = "https://jsonplaceholder.typicode.com/posts/1" #gerçek, herkese açık bir test API'si (sahte blog verisi döndürür)

response = httpx.get(url) # GET isteği (bu adresteki veriyi ver)

print("--İstek--")
print(f"Metot: GET")
print(f"URL: {url}")

print("\n--Cevap--")
print(f"Durum kodu: {response.status_code}") # 200 = başarılı, 404 = bulunamadı, 500 = sunucu hatası
print(f"İçerik tipi: {response.headers['content-type']}") #application/json

print("\n--Gövde (JSON)--")
data = response.json() #JSON metnini Python dict'ine çevirir (deserialize!)
print(f"Tip: {type(data)}")
print(f"Başlık: {data['title']}")

