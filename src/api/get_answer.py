import requests

from src.models.Question import Question
from src.models.Answer import Answer


async def get_answer(question: Question) -> Answer:
    #
    response = {
        'text': '123',
        'class_1': 'str',
        'class_2': ' str',
    }
    return Answer(**response)
