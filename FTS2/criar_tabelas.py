"""from typing import Optional
from pydantic import BaseModel, validator

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

    @validator('nome')
    def validar_nome(cls, value: str):
        abacate = value.split(' ')
        if len(abacate) < 3:
            raise ValueError('O Nome deve ter nome minimo 3 espacos')
        return value
alunos = [

    Aluno(id=1, nome="Andre vitor granemann", idade=25, email="andre@zuplae"),
    Aluno(id=2, nome="Vitor belli pereira", idade=25, email="andre@zuplae")

]"""


from core.configs import settings
from core.database import engine 
from models.aluno_models import AlunoModel

print("executando pra ver se deu boa")

async def create_table():
    print("entrando na funcao")
    
    async with engine.begin() as conn: 
        await conn.run_sync(settings.DB_BaseModel.metadata.drop_all)
        await conn.run_sync(settings.DB_BaseModel.metadata.create_all)
    
    print('Tabela criada com sucesso')


if __name__ == '__main__':
    import asyncio
    asyncio.run(create_table())

    
