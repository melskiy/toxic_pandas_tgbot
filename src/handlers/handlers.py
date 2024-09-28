"""
Этот модуль содержит обработчики для Telegram-бота, созданного на основе Aiogram.
Бот предназначен для ответов на вопросы пользователей о RuTube.
"""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Импортируем необходимые функции и модели из других модулей
from src.api.get_answer import get_answer  # Функция для получения ответа на вопрос
from src.handlers.keyboard.keyboard import main_kb  # Функция для создания основной клавиатуры
from src.models.Question import Question  # Модель для представления вопроса

# Создаем роутер для обработки сообщений
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
async def process_message(message: Message):
    """
    Обрабатывает текстовые сообщения.
    Анализирует текст сообщения и отправляет соответствующий ответ.
    """
    if message.text == "📖 О боте":
        await message.reply("<b>RuTube Helper Bot</b> - твой персональный помощник. \n"
                            "Нужна помощь с загрузкой видео , продвижением канала  или другими вопросами по <b>RuTube</b>❓\n"
                            "Задай свой вопрос боту. Например: Как подключить монетизацию❓\n"
                            "Получи быстрый и точный ответ.⏱️",parse_mode='HTML')
    elif message.text == "❓ Задать вопрос":
        await message.reply("Задайте ваш вопрос:")
    else:
        try:
            question = Question(text = message.text)
            answer = await get_answer(question)
            await  message.answer(f"Ответ: {answer.text}\nКласс 1: {answer.class_1}\nКласс 2: {answer.class_2}")

        except Exception as e:

            await message.answer(f"Произошла ошибка: {str(e)}")
