from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=200)  # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=6, decimal_places=2)  # баланс(DecimalField)
    age = models.IntegerField(default=0)  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # название игры
    cost = models.DecimalField(max_digits=6, decimal_places=2)  # цена(DecimalField)
    size = models.DecimalField(max_digits=6, decimal_places=2)  # размер файлов игры(DecimalField)
    description = models.TextField()  # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField()  # ограничение возраста 18+ (BooleanField, по умолчанию False)

    # покупатель обладающий игрой (ManyToManyField). У каждого покупателя может быть игра и у каждой
    # игры может быть несколько обладателей.
    buyer = models.ManyToManyField(Buyer, related_name='Games')

    def __str__(self):
        return self.title
