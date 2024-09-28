from pydantic import BaseModel


class Answer(BaseModel):
    text: str
    class_1: str
    class_2: str
