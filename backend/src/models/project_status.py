from enum import Enum


class ProjectStatus(str, Enum):
    todo = "ToDo"
    in_progress = "In Progress"
    done = "done"
