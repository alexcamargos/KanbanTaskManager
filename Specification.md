# Kanban Task Manager

Gestor de tarefas desenvolvido com interface de controle de tarefas no
estilo [Kanban](https://pt.wikipedia.org/wiki/Kanban).

<!-- TOC -->
* [Kanban Task Manager](#kanban-task-manager)
  * [Frontend - Task Manager API](#frontend---task-manager-api)
  * [Backend - Task Manager Application](#backend---task-manager-application)
  * [Especificações da Tarefa](#especificações-da-tarefa)
  * [Especificações do Projeto](#especificações-do-projeto)
  * [Especificações das Prioridades](#especificações-das-prioridades)
  * [Especificações do Status](#especificações-do-status)
  * [Principais Funcionalidades](#principais-funcionalidades)
<!-- TOC -->

## Frontend - Task Manager API

Será desenvolvido utilizando [FastApi](https://fastapi.tiangolo.com).

## Backend - Task Manager Application

Será desenvolvido utilizando [Angular](https://angular.io).

## Especificações da Tarefa

| Tarefa         | Task            |
|----------------|-----------------|
| Identificação  | id              |
| Nome           | name            |
| Detalhes       | details         |
| Status         | status          |
| Prioridade     | priority        |
| Data Criação   | creation_date   |
| Data Alteração | alteration_date |
| ID do Projeto  | project_id      |

## Especificações do Projeto

| Projeto        | Project         |
|:---------------|:----------------|
| Identificação  | id              |
| Nome           | name            |
| Detalhe        | details         |
| Status         | status          |
| Data Criação   | creation_date   |
| Data Alteração | alteration_date |
| ID das Tarefa  | task_id         |

## Especificações das Prioridades

| Prioridades             |
|-------------------------|
| !! Big Rocks            |
| ! Hoje                  |
| Alta (esta semana)      |
| Média (assim que puder) |
| Baixa (semana que vem)  |

## Especificações do Status

| Status      |
|-------------|
| Todo        |
| In Progress |
| Done        |

## Principais Funcionalidades

Permite a criação de tarefas seguindo os seguintes critérios:

- Nome da tarefa
- Descrição da tarefa
- Status da tarefa
- Prioridade da tarefa
- Projeto que a tarefa compõe.

Permite a visualização da lista de tarefas já criadas:

- É possível editar: O Nome, os detalhes, o Status, a Prioridade e o Projeto vinculado.
- Deletar uma tarefa já criada.

Permite a filtragem das tarefas já criadas, pelos seguintes critérios:

- Status
- Prioridade
- Data de Criação
- Projeto
