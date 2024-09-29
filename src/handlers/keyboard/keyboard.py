from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_kb(user_telegram_id: int):
    """
    Создает основную клавиатуру для бота.

    Args:
        user_telegram_id: ID пользователя в Telegram.

    Returns:
        ReplyKeyboardMarkup: Объект клавиатуры с настроенными кнопками.
    """

    # Создаем список списков кнопок. Внутренние списки представляют строки клавиатуры.
    kb_list = [
        [KeyboardButton(text="📖 О боте"), KeyboardButton(text="❓ Задать вопрос")],
    ]

    # Создаем объект клавиатуры с заданными настройками:
    # - keyboard: Список кнопок.
    # - resize_keyboard: Автоматически подгоняет размер клавиатуры под ширину экрана.
    # - one_time_keyboard: Клавиатура исчезает после одного использования.
    # - input_field_placeholder: Текст в поле ввода.
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )

    return keyboard