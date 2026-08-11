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
def list_tasks() -> list[Task]: # tüm görevleri döndürür (READ)
    return tasks

@app.post("/tasks", status_code = 201)
def create_task(payload: Taskcreate) -> Task: # yeni görev oluşturur (CREATE)
    new_id = max((t.id for t in tasks), default = 0) + 1
    task = Task(id = new_id, title = payload.title, priority = payload.priority)
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task: # tek bir görevi döndürür (READ one)
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "Görev bulunamadı")

@app.patch("/tasks/{task_id}")
def complete_task(task_id: int) -> Task: # görevi tamamlandı olarak işaretler (UPDATE)
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
        raise HTTPException(status_code = 404, detail = "Görev bulunamadı")

@app.delete("/tasks/{task_id}", status_code = 204)
def delete_task(task_id: int) -> None:  #görevi siler (DELETE)
    for i, task in (enumerate(tasks)):
        if task.id == task_id:
            tasks.pop(i)
            return
        raise HTTPException(status_code = 404, detail = "Görev bulunamadı")
