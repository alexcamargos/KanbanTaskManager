#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: main.py
#  Version: 0.0.1
#  Summary: Kanban Task Manager
#           This is a simple Task Manager that makes it easy for you to keep
#           track of all Tasks and To Dos.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------
"""Kanban Task Manager.

This is a simple Task Manager that makes it easy for you to keep track of all Tasks and To Dos.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.routers import projects, tasks

app = FastAPI()

ORIGINS = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(projects.router, prefix='/api/v1', tags=["projects"])
app.include_router(tasks.router, prefix='/api/v1', tags=["tasks"])


@app.get('/', tags=['root'])
async def root() -> dict:
    return {'message': 'Kanban Task Manager API V1.'}


@app.get('/health', tags=['health'])
async def health_check() -> dict:
    """Health Check."""
    return {'message': 'All systems are operational.'}


if __name__ == '__main__':
    uvicorn.run(app)
