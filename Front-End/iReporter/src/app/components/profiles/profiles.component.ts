import { Component, OnInit } from '@angular/core';
import {ProfilesService} from "../../services/profiles.service";

@Component({
  selector: 'app-profiles',
  templateUrl: './profiles.component.html',
  styleUrls: ['./profiles.component.css'],
  providers: [ProfilesService]
})
export class ProfilesComponent implements OnInit {
  profiles:any = {pos:[{id:1},{fullname:'testname'},{bio:'bio'}, {organisation:'organisation'},
    {location:'location'}, {profile_pic:'https://res.cloudinary.com/ireporter2022/image/upload/v1656953718/crime5_r8mbnm.jpg'}]};
  selectedProfile: any;

  constructor(private api: ProfilesService) {
    this.getClientsProfiles();
    this.selectedProfile ={id:-1, fullname:'', bio:'', location:'', }
  }
  getClientsProfiles=() =>{
    this.api.getAllClient().subscribe(
      data => {
        this.profiles =data
      },
      error => {
        console.log(error)
      }
    )
  }

  clientClicked = (client:any)=>{
    this.api.getOneClient(client.id).subscribe(
      data => {
        this.selectedProfile = data;
          alert("you have clicked")
      },
      error => {
        console.log(error)
      }
    )
  }


  updateProfile =() =>{
    this.api.updateClient(this.selectedProfile).subscribe(
      data => {
        this.getClientsProfiles();
          alert("profile updated successfully")
      },
      error => {
        console.log(error)
        alert("profile update failed")
      }
    )
  }
  createProfile =() =>{
    this.api.createClient(this.selectedProfile).subscribe(
      data => {
        this.getClientsProfiles();

      },
      error => {
        console.log(error)
      }
    )
  }

  deleteProfile =() =>{
    this.api.deleteClient(this.selectedProfile.id).subscribe(
      data => {
        this.getClientsProfiles();

      },
      error => {
        console.log(error)
      }
    )
  }


  ngOnInit(): void {

  }

}
