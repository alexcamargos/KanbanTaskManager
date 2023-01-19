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

from src.models.project import ProjectModel
from src.schemas.project import ProjectResponse, MultipleProjectResponse


def get_project_response(project) -> ProjectResponse:
    """Get single project response.

    :param project: A single project data.

    :return: TaskResponse: A single task response instance.
    """

    return ProjectResponse.from_project_instance(project=ProjectModel(**project))


def get_multiple_project_response(projects) -> MultipleProjectResponse:
    """Get multiple projects response.

    :param projects: A multiple projects data.

    :return: MultipleTaskResponse: A multiple tasks response instance.
    """

    projects = [ProjectModel(**project) for project in projects]

    return MultipleProjectResponse.from_multiple_project_instance(
        projects=projects,
        projects_count=len(projects),
    )
