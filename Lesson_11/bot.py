import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram import html
from aiogram.filters.command import Command, CommandObject
import random


bot_token = "6840435062:AAHxM_D18nizw9JcTalUDsT_FcMKcskASms"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply("Наразі бот не має команд...")

@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    rand_min = 1
    rand_max = 100
    if command.args is not None:
        args = command.args.split()
        if len(args) == 1:
            rand_max = int(args[0])
        else:
            rand_min, rand_max = int(args[0]), int(args[1])
    await message.answer(f"Згенероване число ({rand_min}-{rand_max}): {html.code(random.randint(rand_min, rand_max))}",
                         parse_mode=ParseMode.HTML)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())