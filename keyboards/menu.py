from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(KeyboardButton('👋 Обо мне'))
main_menu_kb.add(KeyboardButton('⚙️ Мои проекты'))
main_menu_kb.add(KeyboardButton('🧠 Навыки'))
main_menu_kb.add(KeyboardButton('📞 Контакты'))
