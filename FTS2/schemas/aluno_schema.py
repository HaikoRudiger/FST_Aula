from core.configs import settings
from packaging import BaseModel as SCBaseModel

class AlunoSchema(settings.DB_BaseModel):

    __tablename__ = 'alunos'

    id: int
    nome: str
    email: str

    class config():
        orm_mode = True