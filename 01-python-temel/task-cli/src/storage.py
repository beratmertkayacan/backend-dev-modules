#görevleri JSON dosyasına kaydet/oku (nasıl saklanır?)
from __future__ import annotations
import json

from pathlib import Path
from src.models import Task

def load_tasks(path: str | Path) -> list[Task]: #JSON dosyasından görevleri oku,Task listesi döndürür
    file = Path(path)
    
    if not file.exists():
        return[]
    
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
        return [Task.from_dict(item) for item in data]

def save_tasks(path: str | Path, tasks: list[Task]) -> None: #Task listesini JSON dosyasına yazar
    data = [task.to_dict() for task in tasks]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)