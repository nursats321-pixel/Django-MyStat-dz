from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    #каждая функция во views обязательно принимает объект запроса (request)
    data = [
        {'title': 'Первый пост', 'text': 'Django - это пауэр!', 'author': 'Админ'},
        {'title': 'Вопрос', 'text': 'А когда уже чат сделаем?', 'author': 'Студент'},
        {'title': 'Анонс', 'text': 'Чаты будут очень скоро!', 'author': 'Гранд-мастер Максим'},
    ]

    context = {
        'posts': data,
    }

    return render(request, 'main/index.html', context)

def team_view(request):
    members = [
        {'name': 'Макс', 'role': 'Lead Python Dev'},
        {'name': 'Алексей', 'role': 'Frontend engineer'},
        {'name': 'Сьюзи', 'role': 'UX/UI Designer'},
    ]

    context = {
        'team': members,
    }

    return render(request, 'main/team.html', context)

