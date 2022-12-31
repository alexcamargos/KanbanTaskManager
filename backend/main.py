from fastapi import FastAPI
from src.routers import projects

app = FastAPI()

app.include_router(projects.router)


@app.get('/')
async def root():
    return {'message': 'Kanban Task Manager API V1.'}
