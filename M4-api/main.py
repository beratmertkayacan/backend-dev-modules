"""Task API — görevleri HTTP üzerinden yöneten sunucu"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = "Task API")

# Veri modelleri (Pydantic)
class Taskcreate(BaseModel): # istemciden gelen 'yeni görev' verisi (id ve done yok).
    title: str
    priority: str = "medium"

class Task(Taskcreate): # sunucunun sakladığı ve döndürdüğü tam görev.
    id: int
    done: bool = False

tasks: list[Task] = [] # görevleri saklamak için geçici depo (DB gibi düşünülebilir)(M5 -> veritabanı gelecek)


'''endpointler'''
@app.get("/tasks")
def list_tasks() -> list[Task]: #Tüm görevleri döndürür (READ)
    return tasks

@app.post("/tasks", status_code = 201)
def create_task(payload: Taskcreate) -> Task: # Yeni görev oluşturur (CREATE)
    new_id = max((t.id for t in tasks), default = 0) + 1
    task = Task(id = new_id, title = payload.title, priority = payload.priority)
    tasks.append(task)
    return task


