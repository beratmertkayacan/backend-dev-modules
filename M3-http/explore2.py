'''farklı HTTP metotları ve durum kodları'''
import httpx

BASE ="https://jsonplaceholder.typicode.com"

# GET: var olan veriyi oku(read)
r = httpx.get(f"{BASE}/posts/1")
print(f"GET / posts/1 -> {r.status_code} (200 = başarılı, veri geldi)")
 
# POST: yeni veri oluştur(create)
yeni = {"title": "Backend calis", "body": "M3 çalışıyorum", "userId": 1}
r = httpx.post(f"{BASE}/posts", json=yeni)
print(f"POST /posts -> {r.status_code} (201 = oluşturuldu, veri eklendi)")
print(f"Sunucunun döndürdüğü yeni kayıt: {r.json()}")

# Olmayan bir şey iste (404 not found)
r = httpx.get(f"{BASE}/posts/9999")
print(f"GET / posts/9999 -> {r.status_code} (404 = bulunamadı)")
