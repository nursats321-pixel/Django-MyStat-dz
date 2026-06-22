from django.db import models
from django.contrib.auth.models import User # Подтягиваем встроенных юзеров Django

class Message(models.Model):
    # ForeignKey связывает сообщение с конкретным юзером.
    # Если юзера удалят (CASCADE) - его сообщения тоже удалятся
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    text = models.TextField()
    
    # Поле для даты, чтобы сортировать сообщения (само ставит текущее время)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        # Чтобы в админке красиво писалось, кто автор
        return f"{self.author.username}: {self.text[:20]}"