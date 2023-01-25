import { NgModule } from '@angular/core';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';

@NgModule({
  exports: [
    MatToolbarModule,
    MatCardModule,
    MatIconModule,
    MatButtonModule,
    MatDividerModule,
  ],
})
export class AngularMaterialModule {}
