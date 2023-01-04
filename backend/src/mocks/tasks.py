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

import datetime

from ..schemas.task import Task

_task_01 = Task(id=1,
                name='Task 01',
                details='Detailed description of task 01.',
                status=1,
                priority=5,
                creation_date=datetime.date(2022, 12, 15),
                alteration_date=datetime.date(2022, 12, 15),
                project_id=1)

_task_02 = Task(id=2,
                name='Task 02',
                details='Detailed description of task 02.',
                status=2,
                priority=4,
                creation_date=datetime.date(2022, 12, 15),
                alteration_date=datetime.date(2022, 12, 17),
                project_id=1)

_task_03 = Task(id=3,
                name='Task 03',
                details='Detailed description of task 03.',
                status=1,
                priority=4,
                creation_date=datetime.date(2022, 12, 15),
                alteration_date=datetime.date(2022, 12, 20),
                project_id=2)

_task_04 = Task(id=4,
                name='Task 04',
                details='Detailed description of task 04.',
                status=1,
                priority=3,
                creation_date=datetime.date(2022, 12, 15),
                alteration_date=datetime.date(2022, 12, 15),
                project_id=2)

_task_05 = Task(id=5,
                name='Task 05',
                details='Detailed description of task 05.',
                status=3,
                priority=5,
                creation_date=datetime.date(2022, 12, 15),
                alteration_date=datetime.date(2022, 12, 15),
                project_id=3)

_task_06 = Task(id=6,
                name='Task 06',
                details='Detailed description of task 06.',
                status=1,
                priority=2,
                creation_date=datetime.date(2022, 12, 15),
                alteration_date=datetime.date(2022, 12, 16),
                project_id=3)

_task_07 = Task(id=7,
                name='Task 07',
                details='Detailed description of task 07.',
                status=2,
                priority=3,
                creation_date=datetime.date(2022, 12, 16),
                alteration_date=datetime.date(2022, 12, 19),
                project_id=1)

_task_08 = Task(id=8,
                name='Task 08',
                details='Detailed description of task 08.',
                status=1,
                priority=4,
                creation_date=datetime.date(2022, 12, 18),
                alteration_date=datetime.date(2022, 12, 20),
                project_id=1)

_task_09 = Task(id=9,
                name='Task 09',
                details='Detailed description of task 09.',
                status=3,
                priority=5,
                creation_date=datetime.date(2022, 12, 19),
                alteration_date=datetime.date(2022, 12, 20),
                project_id=2)

_task_10 = Task(id=10,
                name='Task 10',
                details='Detailed description of task 10.',
                status=1,
                priority=4,
                creation_date=datetime.date(2022, 12, 20),
                alteration_date=datetime.date(2022, 12, 20),
                project_id=2)

TASKS_LIST = [_task_01, _task_02, _task_03, _task_04, _task_05, _task_06, _task_07, _task_08, _task_09, _task_10]

__all__ = ['TASKS_LIST']
