import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';


import { tap, shareReplay } from 'rxjs/operators';

import jwtDecode from 'jwt-decode';
import * as moment from 'moment';

// import { environment } from '../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  base_url = 'https://ireportermoringa.herokuapp.com/api/'

  constructor(private http:HttpClient) { }
  registerUser(userData:any): Observable<any>{
    return this.http.post('https://ireportermoringa.herokuapp.com/api/client', userData);
  }
  registerAdmin(userData:any): Observable<any>{
    return this.http.post('https://ireportermoringa.herokuapp.com/api/admin', userData);
  }
  // loginUsers(userData:any): Observable<any>{
  //   return this.http.post('https://ireportermoringa.herokuapp.com/api/token', userData);
  // }

  private setSession(access_token:string) {
    // const token = authResult.token;
    const payload = jwtDecode <JWTPayload>(access_token);
    const expiresAt = moment.unix(payload.exp);

    localStorage.setItem('access_token', access_token);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }

  get token(): string {
    return localStorage.getItem('access_token')|| '{}';
  }

  get refresh_token(): string {
    return localStorage.getItem('refresh_token')|| '{}';
  }

  login(userPayLoad: any):Observable<any> {
    return this.http.post<logInResponse>('${this.base_url}token',userPayLoad).pipe(
      tap(response => {
        this.setSession(response.access_token)
        localStorage.setItem('refresh_token', response.refresh_token)
      }),
      shareReplay(),
    )
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('expires_at');
  }

  refreshToken() {
    if (moment().isBetween(this.getExpiration().subtract(1, 'days'), this.getExpiration())) {
      this.http.post<refreshResponse>('${this.base_url}token/refresh/',{refresh: this.refresh_token})
      .pipe(
        tap(response => this.setSession(response.access)),
        shareReplay(),
      ).subscribe();
    }
  }

  getExpiration() {
    const expiration = localStorage.getItem('expires_at');
    const expiresAt = JSON.parse(expiration!);
    return moment(expiresAt);
  }

  isLoggedIn() {
    return moment().isBefore(this.getExpiration());
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }
}

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const access_token = localStorage.getItem('access_token');

    if (access_token) {
      const cloned = req.clone({
        headers: req.headers.set('Authorization', 'JWT '.concat(access_token))
      });

      return next.handle(cloned);
    } else {
      return next.handle(req);
    }
  }
}

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) { }

  canActivate() {
    if (this.authService.isLoggedIn()) {
      this.authService.refreshToken();

      return true;
    } else {
      this.authService.logout();
      this.router.navigate(['login']);

      return false;
    }
  }
}
interface JWTPayload {
  user_id: number;
  username: string;
  email: string;
  exp: number;
}
interface logInResponse {
  access_token: string;
  refresh_token: string;
  user: object;
}
interface refreshResponse {
  access: string;
  refresh: string;
}