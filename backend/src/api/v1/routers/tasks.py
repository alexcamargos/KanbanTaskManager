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
"""

from fastapi import APIRouter, HTTPException
from src.mocks.tasks import TASKS_LIST
from src.models.task_priority import TaskPriority
from src.models.task_status import TaskStatus
from src.schemas.task import Task

router = APIRouter()


@router.get('/tasks')
def get_tasks() -> list[Task]:
    """
    Get all tasks.

    :return list: List of tasks.
    """

    # Serializing a Python namedtuple to json.
    return [task._asdict() for task in TASKS_LIST]


@router.get('/tasks/{task_id}')
def get_task_by_id(task_id: int) -> Task:
    """
    Get a task by id.

    :param task_id: The id of the task.
    :return Task: The task information or a message if the task is not found.
    """

    # Parse the human-readable task id to the index of the task in the list.
    index = task_id - 1

    if task_id <= len(TASKS_LIST):
        # Serializing a Python namedtuple to json.
        return TASKS_LIST[index]._asdict()
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/tasks/status/')
async def get_task_by_status(task_status: TaskStatus) -> list[Task]:
    """
    Get tasks filtered by status.

    :param task_status: Task priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :return list: A list of tasks with the status or a message if no tasks are found.
    """

    if task_status == TaskStatus.todo.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.status == TaskStatus.todo.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_status == TaskStatus.in_progress.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.status == TaskStatus.in_progress.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_status == TaskStatus.done.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.status == TaskStatus.done.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/tasks/priorities/')
async def get_task_by_priority(task_priority: TaskPriority) -> list[Task]:
    """
    Get tasks filtered by priority.

    :param task_priority: Task priority.
                            1 - Big Rocks
                            2 - Today
                            3 - High (esta semana)
                            4 - Regular (assim que puder)
                            5 - Low (semana que vem)

    :return list: A list of tasks with the priority or a message if no tasks are found.
    """

    if task_priority == TaskPriority.big_rocks.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.priority == TaskPriority.big_rocks.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.today.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.priority == TaskPriority.today.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.high.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.priority == TaskPriority.high.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.regular.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.priority == TaskPriority.regular.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.low.value:
        tasks = [task._asdict() for task in TASKS_LIST if task.priority == TaskPriority.low.value]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/tasks/')
async def get_task_by_status_and_priority(task_status: TaskStatus, task_priority: TaskPriority) -> list[Task]:
    """
    Get tasks filtered by status and priority.

    :param task_status: Task priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :param task_priority: Task priority.
                            1 - Big Rocks
                            2 - Today
                            3 - High (esta semana)
                            4 - Regular (assim que puder)
                            5 - Low (semana que vem)

    :return list: A list of tasks with the status and priority or a message if no tasks were found.
    """

    if task_priority == TaskPriority.big_rocks.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.big_rocks.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.todo.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.in_progress.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.done.value:
            tasks = [task for task in tasks if task.status == TaskStatus.done.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.today.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.today.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task for task in tasks if task.status == TaskStatus.todo.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.in_progress.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.done.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.done.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.high.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.high.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.todo.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.in_progress.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.done.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.done.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.regular.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.regular.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.todo.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.in_progress.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.done.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.done.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif task_priority == TaskPriority.low.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.low.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.todo.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.in_progress.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        elif task_status.value == TaskStatus.done.value:
            tasks = [task._asdict() for task in tasks if task.status == TaskStatus.done.value]

            if tasks:
                return tasks
            else:
                raise HTTPException(status_code=404, detail='No projects found.')
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/tasks/project/{project_id}')
async def get_task_by_project(project_id: int) -> list[Task]:
    """
    Get all tasks filtered by project id.

    :param project_id: An id of the project.
    :return list: List of tasks or message if no tasks found.
    """

    # List all project id in TASKS_LIST.
    projects_id = [task.project_id for task in TASKS_LIST]

    if project_id in projects_id:
        tasks = [task._asdict() for task in TASKS_LIST if task.project_id == project_id]

        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')
