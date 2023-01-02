from typing import NamedTuple
import datetime

from ..schemas.status import Status


class Project(NamedTuple):
    id: int
    name: str
    details: str
    status: int
    creation_date: datetime.date
    alteration_date: datetime.date
    tasks_ids: list


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
