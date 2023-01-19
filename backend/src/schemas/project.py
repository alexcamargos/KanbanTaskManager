#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: project.py
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

from datetime import datetime

from pydantic.main import BaseModel

from ..models.project import ProjectModel


class ProjectResponse(BaseModel):
    id: int
    name: str
    details: str
    status: int
    creation_date: datetime
    alteration_date: datetime
    tasks_ids: list

    @classmethod
    def from_project_instance(cls, project: ProjectModel) -> "ProjectResponse":
        return cls(**project.dict())


class MultipleProjectResponse(BaseModel):
    projects: list[ProjectModel]
    projects_count: int

    @classmethod
    def from_multiple_project_instance(
            cls,
            projects: list[ProjectModel],
            projects_count: int) -> "MultipleProjectResponse":
        return cls(projects=[project for project in projects],
                   projects_count=projects_count)
