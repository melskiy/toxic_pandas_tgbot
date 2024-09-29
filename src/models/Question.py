from pydantic import BaseModel

#Модель для хранения вопроса пользователя
class Question(BaseModel):
    question: str