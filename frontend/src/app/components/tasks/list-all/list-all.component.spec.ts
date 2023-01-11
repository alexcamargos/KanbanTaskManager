import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAllTasksComponent } from './list-all.component';

describe('ListAllTasksComponent', () => {
  let component: ListAllTasksComponent;
  let fixture: ComponentFixture<ListAllTasksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ListAllTasksComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(ListAllTasksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
