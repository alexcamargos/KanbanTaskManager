#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: projects.py
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

from fastapi import APIRouter, HTTPException

from src.mocks.projects import PROJECT_LIST
from src.models.status import ProjectStatus
from src.schemas.project import Project

router = APIRouter()


@router.get('/projects')
async def get_projects() -> list[Project]:
    """Get all projects.

    :return list: A list with all projects.
    """

    return [project._asdict() for project in PROJECT_LIST]


@router.get('/projects/{project_id}')
async def get_project(project_id: int) -> Project:
    """
    Get a project by id.

    :param project_id: The id of the project.
    
    :return list: The project information.
    """

    # Parse the human-readable project id to the index of the task in the list.
    index = project_id - 1

    if project_id <= len(PROJECT_LIST):
        return PROJECT_LIST[index]._asdict()
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/projects/')
async def get_projects_by_status(project_status: ProjectStatus) -> list[Project]:
    """
    Get projects with status as filte.

    :param project_status: Task priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :return list: List of projects with the status.
    """

    if project_status == ProjectStatus.todo.value:
        projects = [project._asdict() for project in PROJECT_LIST if project.status == ProjectStatus.todo.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif project_status == ProjectStatus.in_progress.value:
        projects = [project._asdict() for project in PROJECT_LIST if project.status == ProjectStatus.in_progress.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif project_status == ProjectStatus.done.value:
        projects = [project._asdict() for project in PROJECT_LIST if project.status == ProjectStatus.done.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')
