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
    tasks = load_tasks(TASKS_FILE)
    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    print(f"Toplam: {total} | Tamamlanan: {done} | Kalan: {total - done}")

    priorities = Counter(t.priority for t in tasks)
    for name, count in priorities.items():
        print(f" {name}: {count}")

def cmd_remove(args: argparse.Namespace) -> None: # verilen ID'ye sahip görevi siler (!!ID eşleşmeyen herkesi tut)
    tasks = load_tasks(TASKS_FILE)
    remaining = [t for t in tasks if t.id != args.id]
    if len(remaining) == len(tasks): # edge case kontrolü (çıktı yoksa siler)
        print(f"Hata: {args.id} ID'li görev bulunamadı")
        return
    save_tasks(TASKS_FILE, remaining)
    print(f"Görev {args.id} silindi")

def cmd_clear(args: argparse.Namespace) -> None: # tamamlanmış görevleri siler
    tasks = load_tasks(TASKS_FILE)
    remaining = [t for t in tasks if not t.done]
    removed = len(tasks) - len(remaining)
    save_tasks(TASKS_FILE, remaining)
    print(f"Tamamlanmış {removed} görevi silindi")





def build_parser() -> argparse.ArgumentParser: # komut-argüman tanımlar 
    parser = argparse.ArgumentParser(description="Görev yöneticisi")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Yeni görev ekle")
    p_add.add_argument("title", help="Görev başlığı")
    p_add.add_argument(
        "--priority",
        default="medium",
        choices=["low", "medium", "high"],
        help="Öncelik (varsayılan: medium)",
    )
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="Görevleri listele")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="Bir görevi tamamla")
    p_done.add_argument("id", type=int, help="Görev numarası")
    p_done.set_defaults(func=cmd_done)

    p_stats = sub.add_parser("stats", help="İstatistikleri göster")
    p_stats.set_defaults(func=cmd_stats)

    p_remove = sub.add_parser("remove", help="Bir görevi sil")
    p_remove.add_argument("id", type=int, help="Görev numarası")
    p_remove.set_defaults(func=cmd_remove)

    p_clear = sub.add_parser("clear", help = "Tamamlanmış görevleri sil")
    p_clear.set_defaults(func=cmd_clear)

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

'''Gerçek backend’de main.py yerine FastAPI/Flask route’ları olur 
storage.py yerine PostgreSQL + SQLAlchemy
models.py mantığı aynı kalır.

Dosya	      Soruya cevap	            İş dünyasındaki karşılığı
models.py      Veri ne? Kurallar ne?      Entity, Domain Model, DTO mapping
storage.py     Nerede saklanır?           Repository, DAO, Persistence Layer
main.py        Kullanıcı ne yapabilir?    Controller, CLI, API routes (FastAPI’de)'''