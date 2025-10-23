from aiogram import types, Dispatcher
from keyboards.menu import main_menu_kb

def register_handlers(dp: Dispatcher):
    @dp.message_handler(lambda m: m.text and m.text.startswith('👋 Обо мне'))
    async def about_handler(message: types.Message):
        text = (
            "Меня зовут Жандос 👋\n"
            "Я разработчик Telegram-ботов и Python-программ.\n"
            "Создаю полезные, удобные и стабильные решения для бизнеса и фриланса.\n\n"
            "Если вам нужно: каталог, автосбор заявок, интеграция с API — я помогу."
        )
        await message.answer(text, reply_markup=main_menu_kb)
