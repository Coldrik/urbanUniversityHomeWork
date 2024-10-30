from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    games_to_buy = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
        'games_to_buy': games_to_buy
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)

# sys_context = { 'title': 'ИГРЫ'}
# title = 'ИГРЫ'
# games_to_buy = {"Game001": 'Atomic Heart', "Game002": 'Cyberpunk 2077', "Game003": 'PayDay 2'}
#
# sys_context.update(games_to_buy)
# context = sys_context
# print(context)
