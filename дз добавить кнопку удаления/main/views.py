import datetime
import jwt  # Шаг 1: библиотека для токенов
from django.conf import settings  # Наш SECRET_KEY из settings.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Message



# ШАГ 1: ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ (ГЕНЕРАТОР)
def generate_jwt_token(user):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "is_staff": user.is_staff,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token



# ШАГ 2: СТРАНИЦА ЛОГИНА (ВЫДАЕМ ТОКЕН)
def login_view(request):
    if request.method == "POST":
        user_in = request.POST.get("username")
        pass_in = request.POST.get("password")

        user = authenticate(username=user_in, password=pass_in)

        if user is not None:
            token = generate_jwt_token(user)  # Сгенерировали токен
            response = redirect("index")  # Сказали: «Иди на главную»

            # Вшили токен в куки (в карман браузера)
            response.set_cookie("access_token", token, httponly=True)
            return response
        else:
            return render(
                request, "login.html", {"error": "Неверный логин или пароль"}
            )

    return render(request, "login.html")



# ШАГ 3: ГЛАВНАЯ СТРАНИЦА ЧАТА (ПРОВЕРЯЕМ ТОКЕН)
def index(request):
    # Достаем токен из кук, которые прилетели от браузера
    token = request.COOKIES.get("access_token")

    if not token:
        return redirect("login")  # Токена нет — отправляем логиниться

    try:
        # Расшифровываем токен математически с помощью нашего SECRET_KEY
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        current_username = payload[
            "username"
        ]  # Узнали имя без запроса к базе данных

    except jwt.ExpiredSignatureError:
        return render(
            request, "login.html", {"error": "Время сессии истекло. Зайди снова"}
        )
    except jwt.InvalidTokenError:
        return render(
            request, "login.html", {"error": "Токен подделан! Доступ запрещен"}
        )

    # Логика отправки сообщения (POST)
    if request.method == "POST":
        text_content = request.POST.get("text")
        user_obj = User.objects.get(id=payload["user_id"])
        Message.objects.create(author=user_obj, text=text_content)
        return redirect("index")

    # Отображение сообщений (GET)
    all_messages = Message.objects.all().order_by("-created_at")
    return render(
        request,
        "index.html",
        {"messages": all_messages, "username": current_username},
    )
    
    

def logout_view(request):
    response = redirect('login')       
    response.delete_cookie('access_token') 
    return response
