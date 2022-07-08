import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-admin-signup',
  templateUrl: './admin-signup.component.html',
  styleUrls: ['./admin-signup.component.css'],
  providers: [AuthService]
})
export class AdminSignupComponent implements OnInit {
  register: any;

  constructor(public authService: AuthService) { }

  ngOnInit(): void {
    this.register= {username:'',email:'',password:'', password2:''};
  }
  registerUser(){
    this.authService.registerAdmin(this.register).subscribe(
      response=> {
        alert('Admin has been registed successfully!')
      },
      error=> console.log (error)
    );
  }

}
