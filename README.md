# Жандос | Telegram Bot Developer — Portfolio Bot

Это готовый проект Telegram-бота-портфолио, который демонстрирует ваши проекты и навыки.

**Название в приветствии:** Жандос | Telegram Bot Developer

---

## Структура проекта
```
portfolio_bot/
├── main.py
├── config.py
├── requirements.txt
├── Procfile
├── Dockerfile
├── README.md
├── handlers/
│   ├── __init__.py
│   ├── start.py
│   ├── about.py
│   ├── projects.py
│   ├── skills.py
│   └── contacts.py
└── keyboards/
    ├── __init__.py
    └── menu.py
```

## Быстрый запуск (локально)
1. Установите Python 3.9+ и создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate   # windows
pip install -r requirements.txt
```

2. Установите переменные окружения (пример):
```bash
export BOT_TOKEN="ВАШ_TOKEN_ОТ_BOTFATHER"
export ADMIN_ID="ВАШ_TELEGRAM_ID_ЧИСЛОМ"
```

3. Запустите бота (long polling):
```bash
python main.py
```

---

## Развёртывание на хостинге (Render / Railway)
Я включил `Procfile` и `Dockerfile`. Для Render/Railway можно использовать `worker` процесс, запускающий `python main.py`.
1. Загрузите репозиторий на GitHub.
2. На Render создайте Service → Worker и укажите Command: `python main.py`.
3. Добавьте переменные окружения `BOT_TOKEN` и `ADMIN_ID` в настройках сервиса.
4. Деплой завершён — бот запустится как фоновый worker (long polling).

> Альтернатива: настроить webhook. Если нужен webhook — дам инструкции и пример Flask/uvicorn app.

---

## Перенос локальных проектов (твои 2 бота)
1. Скопируй файлы/папки с кодом старых ботов в папку `handlers/` (например `quiz_bot_handlers.py`, `shop_bot_handlers.py`).
2. Импортируй и зарегистрируй хендлеры в `main.py` или добавь роуты в `handlers/__init__.py`.
3. Проверь зависимости и добавь в `requirements.txt` (например `sqlite3`, `aiogram` и др.).

Если хочешь — помогу встроить твои старые обработчики прямо сейчас: отправь структуру или основные файлы, и я адаптирую их под этот проект.
