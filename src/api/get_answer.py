import requests

from src.models.Question import Question
from src.models.Answer import Answer

async def get_answer_stream(question: Question) -> Answer:
    """
    Асинхронно получает ответ на вопрос с использованием потокового подхода.

    Аргументы:
        question (Question): Объект вопроса, который будет сериализован и отправлен.

    Возвращает:
        Answer: Объект ответа, содержащий полученный ответ.

    Исключения:
        Exception: Если возникает ошибка во время запроса или обработки.
    """

    # URL для отправки запроса на получение ответа
    url = "https://genuinely-epic-frogfish.cloudpub.ru/predict"
    # Заголовки запроса, указывающие на тип содержимого
    headers = {"Content-Type": "application/json"}

    # Отправка POST-запроса с сериализованным объектом вопроса
    answer = requests.post(url, headers=headers, json=question.model_dump()).json()
    # Возвращение объекта ответа, содержащего ответ на вопрос
    return Answer(answer=answer['answer'])

