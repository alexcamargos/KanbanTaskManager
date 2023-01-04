from fastapi import APIRouter, HTTPException

from src.mocks.projects import PROJECT_LIST
from src.models.project_status import ProjectStatus

router = APIRouter()


@router.get('/projects')
async def get_projects() -> list:
    """Get all projects.

    :return str: String with all projects information.
    """
    return PROJECT_LIST


@router.get('/projects/{project_id}')
async def get_project(project_id: int) -> list:
    """
    Get a project by id.

    :param project_id: The id of the project.
    :return: The project information.
    """

    # Parse the human-readable project id to the index of the task in the list.
    index = project_id - 1

    if project_id <= len(PROJECT_LIST):
        return PROJECT_LIST[index]
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/projects/')
async def get_projects_by_status(project_status: ProjectStatus) -> list:
    """
    Get projects with status as filte.

    :param project_status: Task priority.
                          1 - Todo
                          2 - In Progress
                          3 - Done

    :return: List of projects with the status.
    """

    if project_status == ProjectStatus.todo.value:
        projects = [project for project in PROJECT_LIST if project.status == ProjectStatus.todo.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif project_status == ProjectStatus.in_progress.value:
        projects = [project for project in PROJECT_LIST if project.status == ProjectStatus.in_progress.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif project_status == ProjectStatus.done.value:
        projects = [project for project in PROJECT_LIST if project.status == ProjectStatus.done.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')
