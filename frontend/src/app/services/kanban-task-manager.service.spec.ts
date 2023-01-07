import { TestBed } from '@angular/core/testing';

import { KanbanTaskManagerService } from './kanban-task-manager.service';

describe('KanbanTaskManagerService', () => {
  let service: KanbanTaskManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KanbanTaskManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
