import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Настройки проекта
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
BOT_NAME = os.getenv("BOT_NAME", "Жандос | Telegram Bot Developer")