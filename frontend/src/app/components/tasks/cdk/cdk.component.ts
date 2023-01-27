import { Component, Input, OnInit } from '@angular/core';
import { CdkDragDrop, transferArrayItem } from '@angular/cdk/drag-drop';

import { Task } from 'src/app/models/task.model';

@Component({
  selector: 'app-cdk',
  templateUrl: './cdk.component.html',
  styleUrls: ['./cdk.component.sass'],
})
export class CdkComponent implements OnInit {
  @Input() tasks!: Task[];

  todo: Task[];
  inProgress: Task[];
  done: Task[];

  constructor() {
    this.todo = [];
    this.inProgress = [];
    this.done = [];
  }

  ngOnInit(): void {
    this.processTasks();
  }

  private processTasks(): void {
    this.todo = this.tasks.filter((task) => task.status === 1);
    this.inProgress = this.tasks.filter((task) => task.status === 2);
    this.done = this.tasks.filter((task) => task.status === 3);
  }

  editTask(list: string, task: Task): void {}

  dropTask(event: CdkDragDrop<Task[]>): void {
    if (event.previousContainer === event.container) {
      return;
    }
    if (!event.container.data || !event.previousContainer.data) {
      return;
    }

    transferArrayItem(
      event.previousContainer.data,
      event.container.data,
      event.previousIndex,
      event.currentIndex
    );
  }
}
