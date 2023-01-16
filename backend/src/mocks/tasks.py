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

_task_01: dict[str, int | str | datetime] = {
    'id': 1,
    'name': 'Task number 01',
    'details': 'Detailed description of Task number 01.',
    'status': 1,
    'priority': 5,
    'creation_date': datetime(2022, 12, 15),
    'alteration_date': datetime(2022, 12, 15),
    'project_id': 1
}

_task_02: dict[str, int | str | datetime] = {
    'id': 2,
    'name': 'Task number 02',
    'details': 'Detailed description of Task number 02.',
    'status': 2,
    'priority': 4,
    'creation_date': datetime(2022, 12, 15),
    'alteration_date': datetime(2022, 12, 17),
    'project_id': 1
}

_task_03: dict[str, int | str | datetime] = {
    'id': 3,
    'name': 'Task number 03',
    'details': 'Detailed description of Task number 03.',
    'status': 1,
    'priority': 4,
    'creation_date': datetime(2022, 12, 15),
    'alteration_date': datetime(2022, 12, 20),
    'project_id': 2
}

_task_04: dict[str, int | str | datetime] = {
    'id': 4,
    'name': 'Task number 04',
    'details': 'Detailed description of Task number 04.',
    'status': 1,
    'priority': 3,
    'creation_date': datetime(2022, 12, 15),
    'alteration_date': datetime(2022, 12, 15),
    'project_id': 2
}

_task_05: dict[str, int | str | datetime] = {
    'id': 5,
    'name': 'Task number 05',
    'details': 'Detailed description of Task number 05.',
    'status': 3,
    'priority': 5,
    'creation_date': datetime(2022, 12, 15),
    'alteration_date': datetime(2022, 12, 15),
    'project_id': 3
}

_task_06: dict[str, int | str | datetime] = {
    'id': 6,
    'name': 'Task number 06',
    'details': 'Detailed description of Task number 06.',
    'status': 1,
    'priority': 2,
    'creation_date': datetime(2022, 12, 15),
    'alteration_date': datetime(2022, 12, 16),
    'project_id': 3
}

_task_07: dict[str, int | str | datetime] = {
    'id': 7,
    'name': 'Task number 07',
    'details': 'Detailed description of Task number 07.',
    'status': 2,
    'priority': 3,
    'creation_date': datetime(2022, 12, 16),
    'alteration_date': datetime(2022, 12, 19),
    'project_id': 1
}

_task_08: dict[str, int | str | datetime] = {
    'id': 8,
    'name': 'Task number 08',
    'details': 'Detailed description of Task number 08.',
    'status': 1,
    'priority': 4,
    'creation_date': datetime(2022, 12, 18),
    'alteration_date': datetime(2022, 12, 20),
    'project_id': 1
}

_task_09: dict[str, int | str | datetime] = {
    'id': 9,
    'name': 'Task number 09',
    'details': 'Detailed description of Task number 09.',
    'status': 3,
    'priority': 5,
    'creation_date': datetime(2022, 12, 19),
    'alteration_date': datetime(2022, 12, 20),
    'project_id': 2
}

_task_10: dict[str, int | str | datetime] = {
    'id': 10,
    'name': 'Task number 10',
    'details': 'Detailed description of Task number 10.',
    'status': 1,
    'priority': 4,
    'creation_date': datetime(2022, 12, 20),
    'alteration_date': datetime(2022, 12, 20),
    'project_id': 2
}

TASKS_LIST = [_task_01, _task_02, _task_03, _task_04, _task_05, _task_06, _task_07, _task_08, _task_09, _task_10]

__all__ = ['TASKS_LIST']
