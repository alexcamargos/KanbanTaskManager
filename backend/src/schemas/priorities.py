#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: priorities.py
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

from pydantic import BaseModel


class Priorities(BaseModel):
    """Status schema.

    Attributes:
        big_rocks (int): Big Rocks - The most important tasks.
        today (int): Today - Tasks that need to be done today.
        high (int): High - Tasks that need to be done soon.
        regular (int): Regular - Tasks that need to be done in the near future.
        low (int): Low - Tasks that need to be done in the distant future.
    """

    big_rocks: int = 1
    today: int = 2
    high: int = 3
    regular: int = 4
    low: int = 5
