from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
from config import ADMIN_ID, BOT_NAME

from keyboards.menu import main_menu_kb
from handlers import start, about, projects, skills, contacts

# Загружаем .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрируем обработчики
start.register_handlers(dp)
about.register_handlers(dp)
projects.register_handlers(dp)
skills.register_handlers(dp)
contacts.register_handlers(dp)

if __name__ == '__main__':
    print(f"Запуск {BOT_NAME}...")
    executor.start_polling(dp, skip_updates=True)