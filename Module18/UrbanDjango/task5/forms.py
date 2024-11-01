from django import forms
from django.core.validators import RegexValidator

class UserRegister (forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(max_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль:')

    age = forms.CharField(max_length=3,
                          validators=[RegexValidator(regex=r'^\d+$',  # только цифры
                                                     message='Введите только цифры.',
                                                     code='invalid')],
                          label='Введите свой возраст:',
                          widget=forms.NumberInput())

