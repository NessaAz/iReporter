import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ProfilesService {

  baseurl=  "https://ireportermoringa.herokuapp.com/api";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http:HttpClient) { }
  getAllAdmins(): Observable<any>{
    return this.http.get(this.baseurl+'/adminprofiles', {headers: this.httpHeaders});
  }

  getOneAdmin(id:number): Observable<any>{
    return this.http.get(this.baseurl+'/admins/' + id + '/', {headers: this.httpHeaders});
  }

  updateAdmin(admin:any): Observable<any>{
    const body = {profile_pic: admin.profile_pic, fullname:admin.fullname, organisation:admin.organisation, location:admin.location}
    return this.http.put(this.baseurl+'/admins/' + admin.id + '/', body,
      {headers: this.httpHeaders});
  }

  createAdmin(admin:any): Observable<any>{
    const body = {profile_pic: admin.profile_pic, fullname:admin.fullname, organisation:admin.organisation, location:admin.location }
    return this.http.post(this.baseurl+'/adminprofiles', body,{headers: this.httpHeaders});
  }

  deleteAdmin(id:any): Observable<any> {
    return this.http.delete(this.baseurl + '/admins/' + id + '/',
      {headers: this.httpHeaders});
  }

  getAllClient(): Observable<any>{
    return this.http.get(this.baseurl+'/clientsprofiles', {headers: this.httpHeaders});
  }
  getOneClient(id:number): Observable<any>{
    return this.http.get(this.baseurl+'/clients/' + id + '/', {headers: this.httpHeaders});
  }

  updateClient(client:any): Observable<any>{
    const body = {profile_pic: client.profile_pic, fullname:client.fullname, organisation:client.organisation, location:client.location}
    return this.http.put(this.baseurl+'/clients/' + client.id + '/', body,
      {headers: this.httpHeaders});
  }

  createClient(client:any): Observable<any>{
    const body = {user_id: client.user_id, profile_pic: client.profile_pic, fullname:client.fullname,
      organisation:client.organisation, location:client.location, bio:client.bio }
    return this.http.post(this.baseurl+'/clientsprofiles', body,{headers: this.httpHeaders});
  }

  deleteClient(id:any): Observable<any> {
    return this.http.delete(this.baseurl + '/clients/' + id + '/',
      {headers: this.httpHeaders});
  }
}
