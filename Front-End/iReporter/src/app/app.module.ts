import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PostsComponent } from './components/posts/posts.component';
import {FormsModule} from "@angular/forms";
import { InterventionsComponent } from './components/interventions/interventions.component';
import { TimePipe } from './pipes/time.pipe';
import { LandingComponent } from './components/landing/landing.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';

@NgModule({
  declarations: [
    AppComponent,
    PostsComponent,
    InterventionsComponent,
    TimePipe,
    LandingComponent,
    DashboardComponent,
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule,
    ],

  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
