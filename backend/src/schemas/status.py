#!/usr/bin/env python
# encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: status.py
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


class Status(BaseModel):
    """Status schema.

    Attributes:
        todo (int): Item is not started.
        in_progress (int): Item is in progress.
        done (int): Item is done.
    """

    todo: int = 1
    in_progress: int = 2
    done: int = 3
