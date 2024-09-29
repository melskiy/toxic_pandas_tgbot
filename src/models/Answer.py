from pydantic import BaseModel

#Модель ответа модели
class Answer(BaseModel):
    answer: str
    class_1: str = 'class1'
    class_2: str = 'class2'
