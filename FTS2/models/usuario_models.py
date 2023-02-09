from core.configs import settings
from sqlalchemy import Column, Integer, String

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id: int = Column(Integer, primary_key= True, autoincrement= True)
    nome: str = Column(String(40))
    idade: int = Column(Integer)


    