import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AngularMaterialModule } from './material.module';

import { TaskPriorityPipe } from './pipes/task-priority.pipe';
import { TaskStatusPipe } from './pipes/task-status.pipe';

import { HeaderComponent } from './components/shared/header/header.component';
import { TaskComponent } from './components/shared/task/task.component';

import { AppRoutingModule } from './routes/app-routing.module';
import { AppComponent } from './components/app-root/app-root.component';
import { ListAllTasksComponent } from './components/tasks/list-all/list-all.component';
import { CdkComponent } from './components/tasks/cdk/cdk.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskPriorityPipe,
    TaskStatusPipe,
    TaskComponent,
    ListAllTasksComponent,
    HeaderComponent,
    CdkComponent,
  ],
  imports: [
    AngularMaterialModule,
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
  ],
  providers: [HttpClientModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
