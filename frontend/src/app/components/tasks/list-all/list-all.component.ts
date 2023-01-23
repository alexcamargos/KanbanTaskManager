import { Component, OnInit } from '@angular/core';

import { KanbanTaskManagerService } from '../../../services/kanban-task-manager.service';
import { Task } from '../../../models/task.model';

@Component({
  selector: 'app-list-all',
  templateUrl: './list-all.component.html',
  styleUrls: ['./list-all.component.sass'],
})
export class ListAllTasksComponent implements OnInit {
  allTasks: Task[] | any;
  tasks_count: number | any;

  constructor(private service: KanbanTaskManagerService) {
    this.allTasks = [];
  }

  ngOnInit(): void {
    this.getAllTasks();
  }

  getAllTasks() {
    this.service.getAllTasks().subscribe({
      next: (response) => {
        this.allTasks.push(response.tasks);
        this.tasks_count = response.total;
      },
      error: (error) => console.error(error),
      complete: () => console.info('Fetch data complete!'),
    });
  }
}
