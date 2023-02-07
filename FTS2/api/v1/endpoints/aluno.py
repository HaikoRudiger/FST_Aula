from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.aluno_models import AlunoModel
from schemas.aluno_schema import AlunoSchema
from core.deps import get_session

router = APIRouter()



@router.get('/', response_model=List[AlunoSchema])
async def get_alunos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel)
        result = await session.execute(query)
        alunos = List[AlunoModel] = result.scalars().all()

        return alunos


@router.get('/{aluno_id}', response_model=AlunoSchema, status_code=status.HTTP_200_OK)
async def get_aluno( aluno_id:int, db: AsyncSession = Depends(get_session)):
    async with db as session: 
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno = result.scalar_one_or_none()
        if aluno:
            return aluno

        else:
            HTTPException(detail='Aluno')    

