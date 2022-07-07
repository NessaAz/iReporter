import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http:HttpClient) { }
  registerUser(userData:any): Observable<any>{
    return this.http.post('https://ireportermoringa.herokuapp.com/api/client', userData);
  }
  registerAdmin(userData:any): Observable<any>{
    return this.http.post('https://ireportermoringa.herokuapp.com/api/admin', userData);
  }
  loginUsers(userData:any): Observable<any>{
    return this.http.post('https://ireportermoringa.herokuapp.com/api/token', userData);
  }
}
