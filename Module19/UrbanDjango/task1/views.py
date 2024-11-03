from django.shortcuts import render
from django.views.generic import TemplateView
from typing import List
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.

# userList = ['Sam', 'Max', 'Subzero', 'Rex']

def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    # games_to_buy = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    Games_to_buy = Game.objects.all()
    context = {
        'title': title,
        'games_to_buy': Games_to_buy
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)


'''
БЛОК РЕГИСТРАЦИИ
'''


def validation(username, password, repeat_password, age) -> str | list[str | bool]:
    userList = getDBValue(Buyer)
    if int(age) < 18:
        return ['Вы должны быть старше 18', False]
    if username in userList:
        return ['Пользователь уже существует', False]
    if password != repeat_password:
        return ['Пароли не совпадают', False]

    return [f'Приветствуем {username}!', True]


def getDBValue(tableName):
    return list(tableName.objects.values_list('name', flat=True))


def sign_up_by_django(request):
    error = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # обработка данных
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Дальнейшая логика

            message, valid = validation(username, password, repeat_password, age)

            if valid:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(message)
            else:
                error = message

        else:
            return HttpResponse("Что-то пошло не так")

    else:
        form = UserRegister()
    info = {'form': form, 'error': error}
    return render(request, 'registration_page.html', context=info)


def sign_up_by_html(request):
    error = ''
    if request.method == 'POST':
        # Получаем данные

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Дальнейшая логика
        message, valid = validation(username, password, repeat_password, age)

        if valid:
            return HttpResponse(message)
        else:
            error = message

    info = {'error': error}

    return render(request, 'registration_page.html', context=info)
