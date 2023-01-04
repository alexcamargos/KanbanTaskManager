import datetime
from typing import NamedTuple


class Project(NamedTuple):
    id: int
    name: str
    details: str
    status: int
    creation_date: datetime.date
    alteration_date: datetime.date
    tasks_ids: list
