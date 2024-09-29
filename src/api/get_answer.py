
import requests

from src.models.Question import Question
from src.models.Answer import Answer

async def get_answer_stream(question: Question) -> Answer:
    """
    Asynchronously fetches an answer to a question using a streaming approach.

    Args:
        question (Question): The question object to be serialized and sent.

    Returns:
        Answer: The response object containing the retrieved answer.

    Raises:
        Exception: If an error occurs during the request or processing.
    """

    url = "https://ardently-sovereign-coonhound.cloudpub.ru/qa"
    headers = {"Content-Type": "application/json"}

    answer = requests.post(url, headers=headers, json=question.model_dump()).json()
    return Answer(answer = answer['answer'])

