import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
@Injectable({
  providedIn: 'root'
})
export class InterventionsService {
  baseurl=  "http://127.0.0.1:8000/api";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http:HttpClient) { }

  getAllIntervention(): Observable<any>{
    return this.http.get(this.baseurl+'/interventions', {headers: this.httpHeaders});
  }

  getOneIntervention(id:number): Observable<any>{
    return this.http.get(this.baseurl+'/intervationrequest/' + id + '/', {headers: this.httpHeaders});
  }

  updateIntervention(intervention:any): Observable<any>{
    const body = {title: intervention.title, info:intervention.info, location:intervention.location }
    return this.http.put(this.baseurl+'/intervationrequest/' + intervention.id + '/', body,
      {headers: this.httpHeaders});
  }

  createIntervention(intervention:any): Observable<any>{
    const body = {image: intervention.image, title: intervention.title, info:intervention.info, location:intervention.location }
    return this.http.post(this.baseurl+'/interventions', body,{headers: this.httpHeaders});
  }

  deleteIntervention(id:any): Observable<any> {
    return this.http.delete(this.baseurl + '/intervationrequest/' + id + '/',
      {headers: this.httpHeaders});
  }
}
