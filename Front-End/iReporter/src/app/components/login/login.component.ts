import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth.service";
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [AuthService]
})
export class LoginComponent implements OnInit {
  login: any;

  constructor(public authService: AuthService, private router: Router) { }
  goPost() {
    this.router.navigate(['/', 'redflags']);
  }

  ngOnInit(): void {
    this.login= {username:'', password:''};
  }
  loginUser(){
    this.authService.loginUsers(this.login).subscribe(
      response=> {
        alert('Login successfully!')
        this.goPost()
      },
      error=>{
        alert('You have entered an invalid username or password!')
      }
    );
  }
}
