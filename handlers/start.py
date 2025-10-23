from aiogram import types, Dispatcher
from keyboards.menu import main_menu_kb
from config import BOT_NAME

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start', 'help'])
    async def cmd_start(message: types.Message):
        text = f"Привет!\n\nЯ — {BOT_NAME}.\nЭтот бот покажет мои проекты и навыки как разработчика Telegram-ботов.\n\nВыбери раздел в меню ниже."
        await message.answer(text, reply_markup=main_menu_kb)
