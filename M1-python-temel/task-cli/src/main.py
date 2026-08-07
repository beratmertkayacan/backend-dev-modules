#komut satır arayüzÜ (CLI): görevleri terminalden yönet (kullanıcı nasıl kullanacak? storage ile models arası köprü)
from __future__ import annotations
import argparse

from collections import Counter
from src.models import Task
from src.storage import load_tasks, save_tasks

TASKS_FILE = "tasks.json"

def cmd_add(args: argparse.Namespace) -> None: # yeni görev ekler
    tasks = load_tasks(TASKS_FILE)
    new_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id = new_id, title = args.title, priority = args.priority)
    tasks.append(task)
    save_tasks(TASKS_FILE, tasks)
    print(f"Görev eklendi: {task}")

def cmd_list(args: argparse.Namespace) -> None: # tüm görevleri listeler
    tasks = load_tasks(TASKS_FILE)
    if not tasks:
        print("Henüz görev yok")
        return
    for task in tasks:
        print(task)

def cmd_done(args: argparse.Namespace) -> None: # verilen ID'ye sahipgörevi tamamlandı işaretler
    tasks = load_tasks(TASKS_FILE)
    for task in tasks:
        if task.id == args.id:
            task.mark_done()
            save_tasks(TASKS_FILE, tasks)
            print(f"Görev {task} tamamlandı")
            return
    print(f"Hata: {args.id} ID'li görev bulunamadı")

def cmd_stats(args: argparse.Namespace) -> None: #  özet istatistikleri gösterir