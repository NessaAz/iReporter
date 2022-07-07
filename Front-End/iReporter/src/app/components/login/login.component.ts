import { Component, OnInit } from '@angular/core';
import {AuthService} from "../../services/auth.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [AuthService]
})
export class LoginComponent implements OnInit {
  login: any;

  constructor(public authService: AuthService) { }

  ngOnInit(): void {
    this.login= {username:'', password:''};
  }
  loginUser(){
    this.authService.loginUsers(this.login).subscribe(
      response=> {

        alert('User has been Login successfully!')
      },
      error=>{
        alert('You have entered an invalid username or password!')
      }
    );
  }
}
