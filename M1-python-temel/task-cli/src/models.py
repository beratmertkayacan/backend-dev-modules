#görevleri temsil eden sınıf (veri ne?)
from __future__ import annotations

class Task:
    def __init__(
        self,
        id: int,
        title: str,
        priority: str ='medium',
        done: bool = False,
    ) -> None:
        self.id = id
        self.title = title
        self.priority = priority
        self.done = done

    def mark_done(self) -> None:
        self.done = True # görev tamamlandı olarak işaret

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'priority': self.priority,
            'done': self.done,
        } # görevi JSON'a yazılabilir sözlüğe çevir

    @classmethod
    def from_dict(cls, data: dict) -> Task: #sözlükten task nesnesi üretir(JSON'dan okunurken kullanılır)
        return cls(
            id = data['id'],
            title = data['title'],
            priority = data.get('priority', 'medium'),
            done = data.get('done', False),
        )

    def __repr__(self) -> str: #nesneyi okunur biçimde göster
        status = 'tamamlandı' if self.done else 'yapılmadı'
        return f'[{status}] #{self.id} {self.title} ({self.priority})'
    
