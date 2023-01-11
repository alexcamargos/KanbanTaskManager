import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'taskPriority',
})
export class TaskPriorityPipe implements PipeTransform {
  transform(value: number, ...args: unknown[]): unknown {
    if (value === 1) {
      return 'Big Rocks';
    } else if (value === 2) {
      return 'Today';
    } else if (value === 3) {
      return 'High';
    } else if (value === 4) {
      return 'Regular';
    } else {
      return 'Low';
    }
  }
}
