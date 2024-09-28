from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="📖 О боте"), KeyboardButton(text="❓ Задать вопрос")],
        [KeyboardButton(text="⚙️ Админ панель"), KeyboardButton(text="📚 Каталог")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard