import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {FormsModule} from "@angular/forms";
import { LoginComponent } from './components/login/login.component';
import {PostsComponent} from './components/posts/posts.component';
import { SignupComponent } from './components/signup/signup.component';
import { AdminSignupComponent } from './components/admin-signup/admin-signup.component';
import { InterventionsComponent } from './components/interventions/interventions.component';
import { TimePipe } from './pipes/time.pipe';
import { LandingComponent } from './components/landing/landing.component';
<<<<<<< HEAD
import { DashboardComponent } from './components/dashboard/dashboard.component';
=======
import { ProfilesComponent } from './components/profiles/profiles.component';
>>>>>>> 9b773968fc79ebe5330ee3ced4cdb22dde2efd95

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    LoginComponent,
    InterventionsComponent,
    AdminSignupComponent,
    PostsComponent,
    TimePipe,
    LandingComponent,
<<<<<<< HEAD
    DashboardComponent,
=======
    ProfilesComponent,
>>>>>>> 9b773968fc79ebe5330ee3ced4cdb22dde2efd95
  ],
    imports: [
        AppRoutingModule,
        HttpClientModule,
        FormsModule,
        BrowserModule
    ],

  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
