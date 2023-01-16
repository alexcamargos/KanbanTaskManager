#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: tasks.py
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

This is mock data for the tasks.
"""

from fastapi import APIRouter, HTTPException

from src.core.tasks import get_task_response, get_multiple_tasks_response
from src.mocks.tasks import TASKS_LIST
from src.models.priorities import TaskPriority
from src.models.status import TaskStatus
from src.schemas.task import TaskResponse, MultipleTaskResponse

router = APIRouter()


@router.get('/tasks', response_model=MultipleTaskResponse)
def get_tasks() -> MultipleTaskResponse:
    """
    Get all tasks.

    :return MultipleTaskResponse: An instance of MultipleTaskResponse.
    """

    return get_multiple_tasks_response(TASKS_LIST)


@router.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task_by_id(task_id: int) -> TaskResponse:
    """
    Get a task by id, if ID is not found, raise a HTTPException with status code 404.

    :param task_id: The id of the task.

    :return TaskResponse: An instance of TaskResponse or a message if the task is not found.
    """

    # Parse the human-readable task id to the index of the task in the list.
    index = task_id - 1

    try:
        return get_task_response(TASKS_LIST[index])
    except IndexError:
        raise HTTPException(status_code=404, detail=f'Task with ID #{task_id} not found.')


@router.get('/tasks/status/', response_model=MultipleTaskResponse)
async def get_task_by_status(task_status: TaskStatus) -> MultipleTaskResponse:
    """
    Get tasks filtered by status, if status is not found return a empty list.

    :param task_status: TaskResponse priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :return MultipleTaskResponse: An instance of MultipleTaskResponse.
    """

    return get_multiple_tasks_response([task for task in TASKS_LIST if task['status'] == task_status])


@router.get('/tasks/priorities/', response_model=MultipleTaskResponse)
async def get_task_by_priority(task_priority: TaskPriority) -> MultipleTaskResponse:
    """
    Get tasks filtered by priority, if the priority is not found return an empty list.

    :param task_priority: TaskResponse priority.
                            1 - Big Rocks
                            2 - Today
                            3 - High (esta semana)
                            4 - Regular (assim que puder)
                            5 - Low (semana que vem)

    :return MultipleTaskResponse: An instance of MultipleTaskResponse.
    """

    return get_multiple_tasks_response([task for task in TASKS_LIST if task['priority'] == task_priority])


@router.get('/tasks/', response_model=MultipleTaskResponse)
async def get_task_by_status_and_priority(
        task_status: TaskStatus,
        task_priority: TaskPriority) -> MultipleTaskResponse:
    """
    Get tasks filtered by status and priority, if status and priority are not found,
    return an empty list.

    :param task_status: TaskResponse priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :param task_priority: TaskResponse priority.
                            1 - Big Rocks
                            2 - Today
                            3 - High (esta semana)
                            4 - Regular (assim que puder)
                            5 - Low (semana que vem)

    :return MultipleTaskResponse: An instance of MultipleTaskResponse.
    """

    return get_multiple_tasks_response(
        [task for task in TASKS_LIST if task['status'] == task_status if task['priority'] == task_priority])


@router.get('/tasks/project/{project_id}', response_model=MultipleTaskResponse)
async def get_task_by_project(project_id: int) -> MultipleTaskResponse:
    """
    Get all tasks filtered by project id, if the project id is not found, return an empty list.

    :param project_id: An id of the project.

    :return MultipleTaskResponse: An instance of MultipleTaskResponse.
    """

    return get_multiple_tasks_response([task for task in TASKS_LIST if task['project_id'] == project_id])
