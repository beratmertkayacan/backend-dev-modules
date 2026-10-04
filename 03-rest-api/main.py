"""Task API: görevleri HTTP üzerinden yöneten sunucu (Modül 03)"""
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

Priority = Literal["low", "medium", "high"]


# Veri modelleri (Pydantic)
class TaskCreate(BaseModel):  # istemciden gelen 'yeni görev' verisi (id ve done yok)
    title: str
    priority: Priority = "medium"


class Task(TaskCreate):  # sunucunun sakladığı ve döndürdüğü tam görev
    id: int
    done: bool = False


tasks: list[Task] = []  # görevleri saklamak için geçici bellek içi depo (veritabanı sonraki adımda bağlanacak)


def find_task(task_id: int) -> Task:
    """Verilen ID'ye sahip görevi döndürür, yoksa 404 hatası fırlatır."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Görev bulunamadı")


# Endpointler
@app.get("/tasks")
def list_tasks() -> list[Task]:  # tüm görevleri döndürür (READ)
    return tasks


@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate) -> Task:  # yeni görev oluşturur (CREATE)
    new_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id=new_id, title=payload.title, priority=payload.priority)
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:  # tek bir görevi döndürür (READ one)
    return find_task(task_id)


@app.patch("/tasks/{task_id}")
def complete_task(task_id: int) -> Task:  # görevi tamamlandı olarak işaretler (UPDATE)
    task = find_task(task_id)
    task.done = True
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int) -> None:  # görevi siler (DELETE)
    tasks.remove(find_task(task_id))
