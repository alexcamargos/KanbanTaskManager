import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

import { TasksResponse } from '../models/tasks.response.model';
import { Task } from '../models/task.model';
import { Project } from '../models/project.model';

@Injectable({
  providedIn: 'root',
})
export class KanbanTaskManagerService {
  private apiUrl: string;
  private tasks: TasksResponse | any;

  constructor(private http: HttpClient) {
    this.apiUrl = environment.apiUrl;
  }

  getAllTasks(): Observable<TasksResponse> {
    return this.http.get<TasksResponse>(`${this.apiUrl}/tasks`);
  }

  getTaskById(id: number): Observable<TasksResponse> {
    return this.http.get<TasksResponse>(`${this.apiUrl}/tasks/${id}`);
  }

  getAllProjects(): Observable<Project> {
    return this.http.get<Project>(`${this.apiUrl}/projects`);
  }

  getProjectById(id: number): Observable<Project> {
    return this.http.get<Project>(`${this.apiUrl}/projects/${id}`);
  }
}
