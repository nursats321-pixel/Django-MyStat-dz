from django.db import models  # Импортируем готовые инструменты для работы с базой данных

class Message(
    models.Model
):  # Создаем класс Message, который Django превратит в таблицу в БД
    author = models.CharField(
        max_length=50
    )  # Создаем текстовое поле для имени автора, максимум 50 символов
    text = models.TextField()  # Создаем большое текстовое поле для самого текста сообщения


