import aiogram
from aiogram import Bot, Dispatcher, types, executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

import API

api = API.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Расчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb.insert(button)
kb.insert(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='formulas')
async def formula(call):
    await call.message.answer('Формула для расчета калорий:')
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
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
