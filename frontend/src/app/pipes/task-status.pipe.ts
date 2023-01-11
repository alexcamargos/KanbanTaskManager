import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'taskStatus',
})
export class TaskStatusPipe implements PipeTransform {
  transform(value: unknown, ...args: unknown[]): unknown {
    if (value === 1) {
      return 'Todo';
    } else if (value === 2) {
      return 'In Progress';
    } else {
      return 'Done';
    }
  }
}
