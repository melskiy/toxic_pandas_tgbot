import os

from aiogram.filters import Command
from aiogram.types import BotCommand
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from src.router.start_router import start_router

# Загрузка переменных окружения из файла .env.
# Это позволяет хранить секретные данные, такие как токен бота, отдельно от кода.
load_dotenv()

# Получение токена бота из переменной окружения.
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

# Создание экземпляра бота с полученным токеном.
bot = Bot(token=bot_token)

# Создание диспетчера для обработки событий.
dp = Dispatcher()


async def start_bot():
    # Вывод сообщения о запуске бота в консоль.
    print('Бот запущен')

    # Добавление маршрутизатора для обработки команд и сообщений.
    dp.include_router(start_router)
    await bot.set_my_commands([BotCommand(command = 'admin',description=
    'Панель оператора'),BotCommand(command='user', description=
    'Панель пользователя')])
    # Запуск процесса обработки событий.
    await dp.start_polling(bot)
