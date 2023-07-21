import os
import logging

from dotenv import load_dotenv
from aiogram import executor, Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tariffs import tariffs

# Configure logging
logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())
ADMINS = [829489904]
# 1011382984


async def set_default_commands(dp):
    await bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустити бота.'),
            types.BotCommand('view_tariffS', 'Показати всі тарифи.'),
            types.BotCommand('view_tariff', 'Знайти тариф.'),
            types.BotCommand('pick_up_tariff', 'Підібрати тариф.')
        ]
    )

async def on_startup(dp):
    await set_default_commands(dp)

comands_board = types.InlineKeyboardMarkup(row_width = 3)
comands_board.add(
        types.InlineKeyboardButton(text='Показати всі тарифи', callback_data='view_tariffS'),
        types.InlineKeyboardButton(text='Знайти тариф', callback_data='view_tariff'),
        types.InlineKeyboardButton(text='Підібрати тариф', callback_data='pick_up_tariff')
    )

@dp.message_handler(commands='start')
async def start(message:types.Message): 
    await message.answer(''' Привіт!
\n Я бот який допоможе тобі переглядати інформацію про тарифи <b>Lifecell</b>.\n 
Обери дію, яку хочеш виконати:\n''', parse_mode='html',
reply_markup=comands_board)
    
if __name__ == "__main__":
    print()
    executor.start_polling(dp, on_startup=on_startup)

    
