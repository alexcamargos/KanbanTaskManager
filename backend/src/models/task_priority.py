from enum import Enum


class TaskPriority(str, Enum):
    big_rocks = "Big Rocks"
    today = "Today"
    high = "High"
    regular = "regular"
    low = "Low"
