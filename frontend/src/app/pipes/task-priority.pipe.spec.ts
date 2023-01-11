import { TaskPriorityPipe } from './task-priority.pipe';

describe('TaskPriorityPipe', () => {
  it('create an instance', () => {
    const pipe = new TaskPriorityPipe();
    expect(pipe).toBeTruthy();
  });
});
