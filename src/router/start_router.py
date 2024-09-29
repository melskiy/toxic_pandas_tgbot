from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.api.get_answer import get_answer_stream
from src.handlers.keyboard.keyboard import main_kb  # Функция для создания основной клавиатуры
from src.models.Question import Question

start_router = Router()

# Обработчик команды /start
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Обрабатывает команду /start.
    Отправляет приветственное сообщение и основную клавиатуру.
    """
    await message.answer('Начнем! Пиши свои вопросы в свободной форме!',reply_markup=main_kb(message.from_user.id))

@start_router.message()
async def process_message(message: Message, bot:Bot):
    """
    Обрабатывает текстовые сообщения.
    Анализирует текст сообщения и отправляет соответствующий ответ.
    """
    if message.text and len(message.text) > 0:
        if message.text == "📖 О боте":
            await message.reply("<b>RuTube Helper Bot</b> - твой персональный помощник. \n"
                                "Нужна помощь с загрузкой видео , продвижением канала  или другими вопросами по <b>RuTube</b>❓\n"
                                "Задай свой вопрос боту. Например: Как подключить монетизацию❓\n"
                                "Получи быстрый и точный ответ.⏱️",parse_mode='HTML')
        elif message.text == "❓ Задать вопрос":
            await message.reply("Задайте ваш вопрос:")
        else:
            try:
                question = Question(question=message.text)
                message_to_edit = await message.answer("Ищу ответ...") # Отправляем начальное сообщение
                answer  = await get_answer_stream(question)
                await bot.edit_message_text(
                    text=answer.answer,
                    chat_id=message.chat.id,
                    message_id=message_to_edit.message_id,
                )
            except Exception as e:
                pass
