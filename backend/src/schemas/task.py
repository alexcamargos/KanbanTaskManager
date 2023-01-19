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

from datetime import datetime

from pydantic import Field
from pydantic.main import BaseModel

from ..models.task import TaskModel


class TaskResponse(BaseModel):
    id: int
    name: str
    details: str
    status: int
    priority: int
    creation_date: datetime
    alteration_date: datetime
    project_id: int

    @classmethod
    def from_task_instance(cls, task: TaskModel) -> "TaskResponse":
        return cls(**task.dict())


class MultipleTaskResponse(BaseModel):
    tasks: list[TaskModel]
    tasks_count: int

    @classmethod
    def from_multiple_task_instance(
            cls, tasks: list[TaskModel],
            tasks_count: int) -> "MultipleTaskResponse":
        return cls(tasks=[task for task in tasks],
                   tasks_count=tasks_count)
