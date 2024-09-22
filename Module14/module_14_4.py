import aiogram
from aiogram import Bot, Dispatcher, types, executor
from crud_function import *

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

import API
# initiate_db () #  Тестовое заполнение таблицы
# add_product() #  Тестовое заполнение таблицы
products = get_all_products()


api = API.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
kb.resize_keyboard=True
button = InlineKeyboardButton(text='Расчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
button3 = InlineKeyboardButton(text='Покупаем', callback_data='buy')
kb.insert(button)
kb.insert(button2)
kb.row(button3)

buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying'),
        InlineKeyboardButton(text='Product2', callback_data='product_buying'),
        InlineKeyboardButton(text='Product3', callback_data='product_buying'),
        InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Формулы расчета')
async def formula(message):
    await message.answer('Формула для расчета калорий:')
    await message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')

@dp.message_handler(text='Расчитать норму калорий')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text='Покупаем')
async def get_buying_list(message):
    i = 1
    for product in products:
        with open(f'pic/pic{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {product [1]} | Описание: {product [2]} | Цена: {product [3]}')
        i += 1
    await message.answer('Выберете продукт для покупки:',
                         reply_markup=buy_menu)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    cal = (float(data['weight']) * 10.0) + (float(data['growth']) * 6.25) - (
            float(data['age']) * 5.0) + 5.0  # расчет для мужчины
    await message.answer(f'Ваша норма калорий {cal}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью. Для расчета нормы калорий нажмите кнопку или напишите Рассчитать')
    await message.answer('Привет! Я бот помогающий твоему здоровью. '
                         'Для расчета нормы калорий нажмите кнопку или напишите Рассчитать',
                         reply_markup=kb)




@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
