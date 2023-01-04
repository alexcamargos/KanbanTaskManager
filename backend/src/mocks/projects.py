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

This is mock data for the projects.
"""

import datetime

from ..schemas.project import Project

_project_01 = Project(id=1,
                      name='Project 01',
                      details='Detailed description of project 01.',
                      status=1,
                      creation_date=datetime.date(2022, 12, 15),
                      alteration_date=datetime.date(2022, 12, 20),
                      tasks_ids=[1, 2, 7, 8])

_project_02 = Project(id=2,
                      name='Project 02',
                      details='Detailed description of project 02.',
                      status=1,
                      creation_date=datetime.date(2022, 12, 15),
                      alteration_date=datetime.date(2022, 12, 20),
                      tasks_ids=[3, 4, 9, 10])

_project_03 = Project(id=3,
                      name='Project 03',
                      details='Detailed description of project 03.',
                      status=3,
                      creation_date=datetime.date(2022, 12, 15),
                      alteration_date=datetime.date(2022, 12, 16),
                      tasks_ids=[5, 6])

PROJECT_LIST = [_project_01, _project_02, _project_03]

__all__ = ['PROJECT_LIST']
