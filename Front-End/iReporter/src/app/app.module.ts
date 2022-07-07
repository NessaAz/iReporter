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
import { ProfilesComponent } from './components/profiles/profiles.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    LoginComponent,
    InterventionsComponent,
    AdminSignupComponent,
    PostsComponent,
    TimePipe,
    ProfilesComponent,
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
