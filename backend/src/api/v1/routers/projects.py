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

from src.core.project import get_project_response, get_multiple_project_response
from src.mocks.projects import PROJECT_LIST
from src.models.status import ProjectStatus
from src.schemas.project import ProjectResponse, MultipleProjectResponse

router = APIRouter()


@router.get('/projects', response_model=MultipleProjectResponse)
async def get_projects() -> MultipleProjectResponse:
    """Get all projects.

    :return MultipleProjectResponse: A MultipleProjectResponse instance.
    """

    return get_multiple_project_response(PROJECT_LIST)


@router.get('/projects/{project_id}', response_model=ProjectResponse)
async def get_project(project_id: int) -> ProjectResponse:
    """
    Get a project by id.

    :param project_id: The id of the project.
    
    :return ProjectResponse: A ProjectResponse instance.
    """

    # Parse the human-readable project id to the index of the task in the list.
    index = project_id - 1

    try:
        return get_project_response(PROJECT_LIST[index])
    except IndexError:
        raise HTTPException(status_code=404, detail=f'Project with ID #{project_id} not found.')



@router.get('/projects/', response_model=MultipleProjectResponse)
async def get_projects_by_status(project_status: ProjectStatus) -> MultipleProjectResponse:
    """
    Get projects with status as filte.

    :param project_status: Task priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :return list: List of projects with the status.
    """

    return get_multiple_project_response([project for project in PROJECT_LIST if project['status'] == project_status])
