from fastapi import APIRouter

from src.mocks.tasks import TASKS_LIST
from src.models.task_status import TaskStatus
from src.models.task_priority import TaskPriority

router = APIRouter()


@router.get('/tasks')
def get_tasks() -> list:
    """
    Get all tasks.

    :return: List of tasks.
    """

    return TASKS_LIST


@router.get('/tasks/{task_id}')
def get_task_by_id(task_id: int):
    """
    Get a task by id.

    :param task_id: The id of the task.
    :return: The task information or a message if the task is not found.
    """

    if task_id <= len(TASKS_LIST):
        return TASKS_LIST[task_id - 1]
    else:
        return 'Task not found.'


@router.get('/tasks/status/')
async def get_task_by_status(status: TaskStatus) -> list | str:
    """
    Get tasks filtered by status.

    :param status: Task status.
    :return: A list of tasks with the status or a message if no tasks are found.
    """

    if status == TaskStatus.todo.value:
        tasks = [task for task in TASKS_LIST if task.status == TaskStatus.todo.value]

        return tasks if tasks else 'No tasks found.'
    elif status == TaskStatus.in_progress.value:
        tasks = [task for task in TASKS_LIST if task.status == TaskStatus.in_progress.value]

        return tasks if tasks else 'No tasks found.'
    elif status == TaskStatus.done.value:
        tasks = [task for task in TASKS_LIST if task.status == TaskStatus.done.value]

        return tasks if tasks else 'No tasks found.'
    else:
        return 'No tasks found.'


@router.get('/tasks/priority/')
async def get_task_by_priority(priority: TaskPriority) -> list | str:
    """
    Get tasks filtered by priority.

    :param priority: Task priority.
    :return: A list of tasks with the priority or a message if no tasks are found.
    """

    if priority == TaskPriority.big_rocks.value:
        tasks = [task for task in TASKS_LIST if task.priority == TaskPriority.big_rocks.value]

        return tasks if tasks else 'No tasks found.'
    elif priority == TaskPriority.today.value:
        tasks = [task for task in TASKS_LIST if task.priority == TaskPriority.today.value]

        return tasks if tasks else 'No tasks found.'
    elif priority == TaskPriority.high.value:
        tasks = [task for task in TASKS_LIST if task.priority == TaskPriority.high.value]

        return tasks if tasks else 'No tasks found.'
    elif priority == TaskPriority.regular.value:
        tasks = [task for task in TASKS_LIST if task.priority == TaskPriority.regular.value]

        return tasks if tasks else 'No tasks found.'
    elif priority == TaskPriority.low.value:
        tasks = [task for task in TASKS_LIST if task.priority == TaskPriority.low.value]

        return tasks if tasks else 'No tasks found.'
    else:
        return 'No tasks found.'


@router.get('/tasks/')
async def get_task_by_status_and_priority(task_status: TaskStatus, task_priority: TaskPriority) -> list | str:
    """
    Get tasks filtered by status and priority.

    :param task_status: Task status.
    :param task_priority: Task priority.
    :return: A list of tasks with the status and priority or a message if no tasks were found.
    """

    if task_priority == TaskPriority.big_rocks.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.big_rocks.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task for task in tasks if task.status == TaskStatus.todo.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task for task in tasks if task.status == TaskStatus.in_progress.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.done.value:
            tasks = [task for task in tasks if task.status == TaskStatus.done.value]

            return tasks if tasks else 'No tasks found.'
        else:
            return 'No tasks found.'
    elif task_priority == TaskPriority.today.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.today.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task for task in tasks if task.status == TaskStatus.todo.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task for task in tasks if task.status == TaskStatus.in_progress.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.done.value:
            tasks = [task for task in tasks if task.status == TaskStatus.done.value]

            return tasks if tasks else 'No tasks found.'
        else:
            return 'No tasks found.'
    elif task_priority == TaskPriority.high.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.high.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task for task in tasks if task.status == TaskStatus.todo.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task for task in tasks if task.status == TaskStatus.in_progress.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.done.value:
            tasks = [task for task in tasks if task.status == TaskStatus.done.value]

            return tasks if tasks else 'No tasks found.'
        else:
            return 'No tasks found.'
    elif task_priority == TaskPriority.regular.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.regular.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task for task in tasks if task.status == TaskStatus.todo.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task for task in tasks if task.status == TaskStatus.in_progress.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.done.value:
            tasks = [task for task in tasks if task.status == TaskStatus.done.value]

            return tasks if tasks else 'No tasks found.'
        else:
            return 'No tasks found.'
    elif task_priority == TaskPriority.low.value:
        tasks = [task for task in TASKS_LIST if
                 task.priority == TaskPriority.low.value and task.status == task_status.value]

        if task_status.value == TaskStatus.todo.value:
            tasks = [task for task in tasks if task.status == TaskStatus.todo.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.in_progress.value:
            tasks = [task for task in tasks if task.status == TaskStatus.in_progress.value]

            return tasks if tasks else 'No tasks found.'
        elif task_status.value == TaskStatus.done.value:
            tasks = [task for task in tasks if task.status == TaskStatus.done.value]

            return tasks if tasks else 'No tasks found.'
        else:
            return 'No tasks found.'
    else:
        return 'No tasks found.'


@router.get('/tasks/project/{project_id}')
async def get_task_by_project(project_id: int) -> list | str:
    """
    Get all tasks filtered by project id.

    :param project_id: An id of the project.
    :return: List of tasks or message if no tasks found.
    """

    # List all project id in TASKS_LIST.
    projects_id = [task.project_id for task in TASKS_LIST]

    if project_id in projects_id:
        tasks = [task for task in TASKS_LIST if task.project_id == project_id]

        return tasks if tasks else 'No tasks found.'
    else:
        return 'No tasks found.'
