#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: project.py
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

from pydantic.main import BaseModel

from .status import ProjectStatus


class ProjectModel(BaseModel):
    id: int
    name: str
    details: str
    status: ProjectStatus
    creation_date: datetime
    alteration_date: datetime
    tasks_ids: list
