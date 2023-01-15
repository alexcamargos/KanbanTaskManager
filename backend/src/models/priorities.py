#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: task_priority.py
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

from enum import IntEnum


class TaskPriority(IntEnum):
    big_rocks = 1
    today = 2
    high = 3
    regular = 4
    low = 5
