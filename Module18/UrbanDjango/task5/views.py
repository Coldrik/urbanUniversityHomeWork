from typing import List

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

userList = ['Sam', 'Max', 'Subzero', 'Rex']


def validation(username, password, repeat_password, age) -> str | list[str | bool]:
    if int(age) < 18:
        return ['Вы должны быть старше 18', False]
    if username in userList:
        return ['Пользователь уже существует', False]
    if password != repeat_password:
        return ['Пароли не совпадают', False]

    return [f'Приветствуем {username}!', True]


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
