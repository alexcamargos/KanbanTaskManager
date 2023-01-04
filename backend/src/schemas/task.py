import datetime
from typing import NamedTuple


class Task(NamedTuple):
    id: int
    name: str
    details: str
    status: int
    priority: int
    creation_date: datetime.date
    alteration_date: datetime.date
    project_id: int
