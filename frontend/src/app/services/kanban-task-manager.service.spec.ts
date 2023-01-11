import { TestBed } from '@angular/core/testing';

import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

import { KanbanTaskManagerService } from './kanban-task-manager.service';

describe('KanbanTaskManagerService', () => {
  let httpClient: HttpClient;
  let httpTestingController: HttpTestingController;
  let service: KanbanTaskManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({ imports: [HttpClientTestingModule] });

    // Inject the http service and test controller for each test
    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);

    service = TestBed.inject(KanbanTaskManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
