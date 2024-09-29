import asyncio
import random

import requests
from aiogram import  Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command

# Предполагается, что в новой версии aiogram есть фильтр для состояний
from aiogram.filters.state import StateFilter

from src.api.get_answer import get_answer_stream
from src.handlers.keyboard.keyboard import main_kb  # Функция для создания основной клавиатуры
from src.models.Question import Question
from src.questions import qa

start_router = Router()

class Dialog(StatesGroup):
    admin = State('admin')
    user = State('user')

def create_keyboard():

    keyboard = types.ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Да'), KeyboardButton(text = 'Нет'), KeyboardButton(text = 'Подсказка')]],
        resize_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:")
    return keyboard

async def get_qa():
    question_answer = qa
    item = random.choice(question_answer)
    return item[0], item[1]

@start_router.message(Command("user"))
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """
    Обрабатывает команду /start.
    Отправляет приветственное сообщение и основную клавиатуру.
    """
    await state.set_state(Dialog.user)
    await message.answer('Начнем! Пиши свои вопросы в свободной форме!',reply_markup=main_kb(message.from_user.id))


@start_router.message(Command("admin"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Dialog.admin)
    question, answer = await get_qa()
    await message.answer(f'<b>Вопрос от пользователя:</b> {question} \n'
                         f' <b>Ответ модели:</b> {answer}',reply_markup=create_keyboard(),parse_mode='HTML')


@start_router.message(StateFilter(Dialog.user))
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

@start_router.message(StateFilter(Dialog.admin))
async def handle_question_yes(message: types.Message):
    if message.text == "Да":
        await message.answer("Ответ отправлен!")
        await asyncio.sleep(1)
        question, answer = await get_qa()
        await message.answer(f'Вопрос от пользователя: \n {question} Ответ модели: {answer}')
    elif message.text == "Нет":
        await message.answer("Пришлите ответ на вопрос")
    elif message.text == "Подсказка":
        url = "https://ardently-sovereign-coonhound.cloudpub.ru/similar"
        headers = {"Content-Type": "application/json"}
        question = Question(question=message.text)
        answer = requests.post(url, headers=headers, json=question.model_dump()).json()
        await message.answer("```"+"Подсказка"+ answer[0]['page_content']+"```",parse_mode=ParseMode.MARKDOWN_V2 )
        await asyncio.sleep(1)
        question, answer =  await get_qa()
        await message.answer(f'<b>Вопрос от пользователя:</b> {question} \n'
                             f' <b>Ответ модели:</b> {answer}', parse_mode='HTML')
    else:
        await asyncio.sleep(1)
        question, answer =  await get_qa()
        await message.answer(f'<b>Вопрос от пользователя:</b> {question} \n'
                             f' <b>Ответ модели:</b> {answer}', parse_mode='HTML')




