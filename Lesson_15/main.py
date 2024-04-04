import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
import random


# -- ІМПОРТИ ДЛЯ РОБОТИ З FSM --

# states.py – файл зі станами, що знаходиться у цій же папці
from states import CalcStates
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
bot = Bot(token="token")
dp = Dispatcher()

# -- РОБОТА З FSM

# Хендлер для команди /calc
@dp.message(Command("calc"))
async def cmd_calc(message: types.Message, state: FSMContext):
    # state: FSMContext — об'єкт, що зберігає інформацію
    # про стан бота для поточного користувача
    await message.answer("Введіть перше число:")
    # Переключення бота у стан CalcStates.first_number
    # (очікування на введення першого числа)
    await state.set_state(CalcStates.first_number)

# Хендлер для отримання повідомлення, коли бот у стані CalcStates.first_number
@dp.message(CalcStates.first_number)
async def get_first_number(message: types.Message, state: FSMContext):
    # try .. except — конструкція для коректної обробки виключень (помилок)
    try:
        # Збереження у пам'ять бота змінної num_1
        await state.update_data(num_1=int(message.text))
        # Якщо в блоці try виникне помилка, буде викличено
        # один з блоків except, що відповідає типу помилки
    except ValueError:
        await message.answer('Введено некоректне значення!')
    except TypeError:
        await message.answer('Число треба відправити текстом!')
    # except Exception буде активовано, якщо не спрацює ні один з
    # попередніх блоків except
    except Exception as error:
        # Виведення інформації про помилку у консоль (тип помилки і посилання)
        logging.error(f'{type(error)}: {error}')
        await message.answer(f'Невідома помилка: {error}')
    else:
        await message.answer('Введіть друге число:')
        # Переключення бота у стан CalcStates.second_number
        # (очікування на введення другого числа)
        await state.set_state(CalcStates.second_number)

# Хендлер для отримання повідомлення, коли бот у стані CalcStates.second_number
# Більшість конструкцій аналогічні з get_first_number
@dp.message(CalcStates.second_number)
async def get_second_number(message: types.Message, state: FSMContext):
    try:
        num_2 = int(message.text)
    except ValueError:
        await message.answer('Введено некоректне значення!')
    except TypeError:
        await message.answer('Число треба відправити текстом!')
    except Exception as error:
        logging.error(f'{type(error)}: {error}')
        await message.answer(f'Невідома помилка: {error}')
    else:
        # Отримання даних з пам'яті бота відносно поточного користувача
        data = await state.get_data()
        # Отримання змінної num_1 з пам'яті бота
        num_1 = data['num_1']
        await message.answer(f'{num_1} + {num_2} = {num_1 + num_2}')
        # Очищення стану бота
        await state.clear()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/help — отримати довідку за командами\n"
        "/roll — генерація випадкового числа"
    )

@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        await message.answer(f'Випадкове число від 1 до {args[0]}: {random.randint(1, int(args[0]))}')
    else:
        await message.answer(f'Випадкове число від 1 до 100: {random.randint(1, 100)}')


@dp.message()
async def all_messages(message: types.Message):
    print(f'{message.from_user.full_name} (id: {message.from_user.id}): {message.text}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())