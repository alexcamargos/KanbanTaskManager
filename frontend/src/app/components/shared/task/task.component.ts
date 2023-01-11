import { Component, Input } from '@angular/core';

import { KanbanTaskManagerService } from '../../../services/kanban-task-manager.service';

import { Task } from '../../../models/task.model';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.sass'],
})
export class TaskComponent {
  @Input() task!: Task;

  project: string;

  constructor(private service: KanbanTaskManagerService) {
    this.project = '';
  }

  ngOnInit(): void {
    this.service.getProjectById(this.task.project_id).subscribe({
      next: (response) => (this.project = response.name),
      error: (error) => console.error(error),
      complete: () => console.info('Fetch data complete!'),
    });
  }
}
