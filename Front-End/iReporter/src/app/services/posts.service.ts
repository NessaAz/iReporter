import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
@Injectable({
  providedIn: 'root'
})
export class PostsService {

  baseurl=  "http://127.0.0.1:8000/api";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http:HttpClient) { }
  getAllRedFlags(): Observable<any>{
    return this.http.get(this.baseurl+'/flaglists', {headers: this.httpHeaders});
  }
  getOneRedFlag(id:number): Observable<any>{
    return this.http.get(this.baseurl+'/raiseflag/' + id + '/', {headers: this.httpHeaders});
  }
  updateRedFlag(redflag:any): Observable<any>{
    const body = {title: redflag.title, info:redflag.info, location:redflag.location }
    return this.http.put(this.baseurl+'/raiseflag/' + redflag.id + '/', body,
      {headers: this.httpHeaders});
  }
  createRedFlag(redflag:any): Observable<any>{
    const body = {image: redflag.image, title: redflag.title, info:redflag.info, location:redflag.location }
    return this.http.post(this.baseurl+'/flaglists', body,{headers: this.httpHeaders});
  }
  deleteRedFlag(id:any): Observable<any> {
    return this.http.delete(this.baseurl + '/raiseflag/' + id + '/',
      {headers: this.httpHeaders});
  }
}
