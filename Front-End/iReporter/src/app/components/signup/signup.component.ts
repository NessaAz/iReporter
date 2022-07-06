import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
  providers:[AuthService]
})
export class SignupComponent implements OnInit {
  register: any;

  constructor(public authService: AuthService) { }

  ngOnInit(): void {
    this.register= {username:'',email:'',password:'', password2:''};
  }
  registerUser(){
    this.authService.registerUser(this.register).subscribe(
      response=> {
        alert('User has been registed successfully!')
      },
      error=> console.log (error)
    );
  }
}
