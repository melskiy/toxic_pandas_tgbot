import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from src.handlers.handlers import start_router

load_dotenv()
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=bot_token)

dp = Dispatcher()


async def start_bot():
    print('Бот запущен')
    dp.include_router(start_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())