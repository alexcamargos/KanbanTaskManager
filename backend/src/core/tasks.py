#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: tasks.py
#  Version: 0.0.1
#  Summary: Kanban Task Manager
#           This is a simple TaskResponse Manager that makes it easy for you to keep
#           track of all Tasks and To Dos.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from datetime import datetime
from typing import Sequence

from src.models.task import TaskModel
from src.schemas.task import TaskResponse, MultipleTaskResponse


def get_task_response(task: dict[str, int | str | datetime]) -> TaskResponse:
    """Get single task response.

    :param task: A single task data.

    :return: TaskResponse: A single task response instance.
    """

    return TaskResponse.from_task_instance(task=TaskModel(**task))


def get_multiple_tasks_response(tasks: Sequence[dict[str, int | str | datetime]]) -> MultipleTaskResponse:
    """Get multiple tasks response.

    :param tasks: A multiple tasks data.

    :return: MultipleTaskResponse: A multiple tasks response instance.
    """

    tasks = [TaskModel(**task) for task in tasks]

    return MultipleTaskResponse.from_multiple_task_instance(
        tasks=tasks,
        tasks_count=len(tasks),
    )
