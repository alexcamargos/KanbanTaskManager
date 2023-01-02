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
