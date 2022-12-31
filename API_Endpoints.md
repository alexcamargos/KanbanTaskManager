# API Endpoints

Um endpoint de API é uma das extremidades de uma conexão de API, onde são recebidas as chamadas de API.

<!-- TOC -->
* [API Endpoints](#api-endpoints)
  * [Tarefas Endpoints](#tarefas-endpoints)
    * [GET /api/v1/tasks](#get-apiv1tasks)
    * [GET /api/v1/tasks/{id}](#get-apiv1tasksid)
    * [GET /api/v1/tasks?status={status}](#get-apiv1tasksstatusstatus)
    * [GET /api/v1/tasks?priority={priority}](#get-apiv1tasksprioritypriority)
    * [GET /api/v1/tasks?project={project}](#get-apiv1tasksprojectproject)
    * [POST /api/v1/tasks](#post-apiv1tasks)
    * [PUT /api/v1/tasks/{id}](#put-apiv1tasksid)
    * [DELETE /api/v1/tasks/{id}](#delete-apiv1tasksid)
  * [Projetos Endpoints](#projetos-endpoints)
    * [GET /api/v1/projects](#get-apiv1projects)
    * [GET /api/v1/projects/{id}](#get-apiv1projectsid)
    * [POST /api/v1/projects](#post-apiv1projects)
    * [PUT /api/v1/projects/{id}](#put-apiv1projectsid)
    * [GET /api/v1/projects?status={status}](#get-apiv1projectsstatusstatus)
    * [DELETE /api/v1/projects/{id}](#delete-apiv1projectsid)
<!-- TOC -->

## Tarefas Endpoints

### GET /api/v1/tasks

Retorna uma lista contendo todas as tarefas.

### GET /api/v1/tasks/{id}

Retorna as informações de uma tarefa específica.

### GET /api/v1/tasks?status={status}

Retorna uma lista contendo todas as tarefas filtradas pelo status.

### GET /api/v1/tasks?priority={priority}

Retorna uma lista contendo todas as tarefas filtradas pela prioridade.

### GET /api/v1/tasks?project={project}

Retorna uma lista contendo todas as tarefas filtradas pelo projeto.

### POST /api/v1/tasks

Cria uma tarefa.

### PUT /api/v1/tasks/{id}

Atualiza as informações de uma tarefa específica.

### DELETE /api/v1/tasks/{id}

Deleta uma tarefa específica.

## Projetos Endpoints

### GET /api/v1/projects

Retorna uma lista contendo todos os projetos.

### GET /api/v1/projects/{id}

Retorna as informações de uma projeto específico.

### POST /api/v1/projects

Cria um novo projeto.

### PUT /api/v1/projects/{id}

Atualiza as informações de um projeto específico.

### GET /api/v1/projects?status={status}

Retorna uma lista contendo todos os projetos filtrados pelo status.

### DELETE /api/v1/projects/{id}

Deleta um projeto específico.
