from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

# Навчити бота відправляти вам якусь цитату у відповідь на команду /saysomething.

@dp.message_handler(commands='saysomethink')
async def saysome(message: types.Message):
    await message.answer(text='Життя дасть тобі те що ти хочеш, коли ти навишся жити щасливо без цього.')


