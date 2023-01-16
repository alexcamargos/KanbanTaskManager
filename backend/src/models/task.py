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

from pydantic import Field
from pydantic.main import BaseModel


class TaskModel(BaseModel):
    id: int
    name: str
    details: str
    status: int
    priority: int
    creation_date: datetime
    alteration_date: datetime
    project_id: int
