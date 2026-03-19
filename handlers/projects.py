from aiogram import types, Dispatcher

async def show_projects(message: types.Message):
    text = (
        "🧠 *Мои проекты:*\n\n"
        "1️⃣ [Order Bot](https://t.me/order_requests_demo_bot)\n"
        "— Бот-магазин для приёма заказов.\n\n"
        "2️⃣ [Quiz Bot](https://t.me/zhan_quiz_demo_bot)\n"
        "— Викторина с вопросами и подсчётом очков.\n\n"
        "3️⃣ [Этот бот](https://t.me/ZhandosPortfolioBot)\n"
        "— Презентация моих навыков Telegram-разработчика."
    )

    await message.answer(text, parse_mode="Markdown")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_projects,
        lambda message: message.text == "⚙️ Мои проекты"
    )