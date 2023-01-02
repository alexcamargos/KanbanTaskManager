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
    if project_id <= len(PROJECT_LIST):
        return PROJECT_LIST[project_id - 1]
    else:
        raise HTTPException(status_code=404, detail='No projects found.')


@router.get('/projects/')
async def get_projects_by_status(status: ProjectStatus) -> list:
    """Get projects filtered by status.

    :param status: Project status.
    :return: List of projects with the status.
    """

    if status == ProjectStatus.todo.value:
        projects = [project for project in PROJECT_LIST if project.status == ProjectStatus.todo.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif status == ProjectStatus.in_progress.value:
        projects = [project for project in PROJECT_LIST if project.status == ProjectStatus.in_progress.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    elif status == ProjectStatus.done.value:
        projects = [project for project in PROJECT_LIST if project.status == ProjectStatus.done.value]

        if projects:
            return projects
        else:
            raise HTTPException(status_code=404, detail='No projects found.')
    else:
        raise HTTPException(status_code=404, detail='No projects found.')
