from django.contrib import (
    admin,
)  # Импортируем стандартную админку Django из коробки
from .models import (
    Message,
)  # Импортируем нашу модель Message из текущей папки (. означает текущая директория)

admin.site.register(
    Message
)  # Регистрируем модель Message, чтобы она появилась в панели управления