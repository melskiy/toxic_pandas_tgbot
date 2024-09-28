from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.api.get_answer import get_answer
from src.handlers.keyboard.keyboard import main_kb
from src.models.Question import Question

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
                         reply_markup=main_kb(message.from_user.id))

@start_router.message()
async def process_message(message: Message):
    if message.text == "📖 О боте":
        await message.reply("<b>RuTube Helper Bot</b> - твой персональный помощник. \n"
                            "Нужна помощь с загрузкой видео , продвижением канала  или другими вопросами по <b>RuTube</b>❓\n"
                            "Задай свой вопрос боту. Например: Как подключить монетизацию❓\n"
                            "Получи быстрый и точный ответ.⏱️",parse_mode='HTML')
    elif message.text == "❓ Задать вопрос":
        await message.reply("Задайте ваш вопрос:")
    elif message.text == "⚙️ Админ панель":
        await message.reply("в разработке")
    elif message.text == "📚 Каталог":
        await message.reply("Тута будут примеры какие нить:\n...")
    else:
        try:
            question = Question(text = message.text)
            answer = await get_answer(question)
            await  message.answer(f"Ответ: {answer.text}\nКласс 1: {answer.class_1}\nКласс 2: {answer.class_2}")

        except Exception as e:

            await message.answer(f"Произошла ошибка: {str(e)}")
