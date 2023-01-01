from fastapi import FastAPI
from src.routers import projects
from src.routers import tasks

app = FastAPI()

app.include_router(projects.router)
app.include_router(tasks.router)


@app.get('/')
async def root():
    return {'message': 'Kanban Task Manager API V1.'}
