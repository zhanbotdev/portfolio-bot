from aiogram import types, Dispatcher
from keyboards.menu import main_menu_kb

def register_handlers(dp: Dispatcher):
    @dp.message_handler(lambda m: m.text and m.text.startswith('📞 Контакты'))
    async def contacts_handler(message: types.Message):
        text = (
            "📞 Контакты:\n"
            "Telegram: @Zhandos281091\n"
            "WhatsApp: +77018477331\n"
            "GitHub: https://github.com/zhanbotdev\n"
            "Freelance: https://freelancehunt.com/yourpage\n\n"
           # "PS: Ты сам добавишь сюда реальные ссылки и никнеймы в config.py."
        )
        await message.answer(text, reply_markup=main_menu_kb)
