import aiogram
from aiogram import Bot, Dispatcher, types, executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

import API

api = API.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
kb.resize_keyboard=True
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
kb.insert(button)
kb.insert(button2)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


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


@dp.message_handler(commands=['информация'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Для расчета нормы калорий напишите Calories',
                         reply_markup=kb)


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)