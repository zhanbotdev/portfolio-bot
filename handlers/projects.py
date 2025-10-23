from aiogram import types, Dispatcher
from keyboards.menu import main_menu_kb

def register_handlers(dp: Dispatcher):
    @dp.message_handler(lambda m: m.text and m.text.startswith('⚙️ Мои проекты'))
    async def projects_handler(message: types.Message):
        text = (
            "🔹 Мои проекты:\n\n"
            "1️⃣ Бот-игра “Умники и умницы”\n"
            "• Викторина с подсчётом очков, таймером и режимом для нескольких игроков.\n"
            "• Технологии: Python, aiogram, SQLite.\n"
            "🔗 Demo: напиши сюда ссылку на бот\n\n"
            "2️⃣ Магазин-бот “Jamto Store”\n"
            "• Каталог, корзина, оформление заказа, уведомления администратору.\n"
            "• Технологии: Python, aiogram, FSM, SQLite.\n"
            "🔗 Demo: напиши сюда ссылку на бот\n\n"
            "Если хочешь — могу отправить подробное описание по каждому проекту и ссылку на исходники."
        )
        await message.answer(text, reply_markup=main_menu_kb)
