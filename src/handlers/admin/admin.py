from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


async def process_admin_panel(message: Message):
    async def get_messages_from_db():

        return [
            {"text": "Сообщение 1"},
            {"text": "Сообщение 2"},
        ]

    messages = await get_messages_from_db()

    if not messages:
        await message.answer("Нет сообщений")
        return

    current_message_index = 0

    def create_keyboard(message_text):
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("Предыдущее", callback_data="prev"),
            InlineKeyboardButton("Удалить", callback_data="delete")
        )
        return keyboard

    async def show_message(index):
        message_text = messages[index]["text"]
        await message.edit_text(message_text, reply_markup=create_keyboard(message_text))

    await show_message(current_message_index)

# ... (остальной код)

@start_router.callback_query()
async def process_callback_query(callback_query: CallbackQuery):
    global current_message_index

    if callback_query.data == "prev":
        current_message_index -= 1
        if current_message_index < 0:
            current_message_index = len(messages) - 1
        await show_message(current_message_index)

    await callback_query.answer()