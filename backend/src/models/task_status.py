from enum import Enum


class TaskStatus(str, Enum):
    todo = "ToDo"
    in_progress = "In Progress"
    done = "done"
