from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "MAS QUE PORR... ????"}

alunos = {
    
    1: "Lirinha",
    2: "Boladao",
    3: "Haiko",
    4: "Guilherme", 

}

@app.get('/aluno')
async def get_aluno():
    return alunos

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True

    )
