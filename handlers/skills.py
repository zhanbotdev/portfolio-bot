from aiogram import types, Dispatcher
from keyboards.menu import main_menu_kb

def register_handlers(dp: Dispatcher):
    @dp.message_handler(lambda m: m.text and m.text.startswith('🧠 Навыки'))
    async def skills_handler(message: types.Message):
        text = (
            "🧠 Мои навыки:\n"
            "• Python (aiogram, telebot)\n"
            "• Работа с API (Telegram, OpenAI)\n"
            "• FSM, базы данных (SQLite, PostgreSQL)\n"
            "• Развёртывание: Render, Railway, Docker, VPS\n"
            "• Git, Github — публикация репозиториев и CI\n\n"
            "Могу быстро подготовить demo-проект под задачу клиента."
        )
        await message.answer(text, reply_markup=main_menu_kb)
