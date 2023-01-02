from fastapi import FastAPI
from src.api.v1.routers import projects, tasks

app = FastAPI()

app.include_router(projects.router, tags=["projects"])
app.include_router(tasks.router, tags=["tasks"])


@app.get('/')
async def root():
    return {'message': 'Kanban Task Manager API V1.'}
