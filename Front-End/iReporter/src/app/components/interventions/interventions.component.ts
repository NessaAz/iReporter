import { Component, OnInit } from '@angular/core';
import {InterventionsService} from "../../services/interventions.service";


@Component({
  selector: 'app-interventions',
  templateUrl: './interventions.component.html',
  styleUrls: ['./interventions.component.css'],
  providers:[InterventionsService]
})
export class InterventionsComponent implements OnInit {
  posts = [{id:1},{url:'testurl'},{title:'test'}, {info:'test'},{location:'location'},{stages:'stages'},
    {created:'created'},{image:'https://res.cloudinary.com/ireporter2022/image/upload/v1656953718/crime5_r8mbnm.jpg'}];
  selectedPost: any;

  constructor(private api: InterventionsService) {
    this.getInterventions();
    this.selectedPost ={id:-1, title:'', info:'', location:'', }
  }

  getInterventions=() =>{
    this.api.getAllIntervention().subscribe(
      data => {
        this.posts =data
      },
      error => {
        console.log(error)
      }
    )
  }

  interventionClicked = (post:any)=>{
    this.api.getOneIntervention(post.id).subscribe(
      data => {
        this.selectedPost = data;

      },
      error => {
        console.log(error)
      }
    )
  }

  updatePost =() =>{
    this.api.updateIntervention(this.selectedPost).subscribe(
      data => {
        this.getInterventions();

      },
      error => {
        console.log(error)
      }
    )
  }
  createPost =() =>{
    this.api.createIntervention(this.selectedPost).subscribe(
      data => {
        this.getInterventions();

      },
      error => {
        console.log(error)
      }
    )
  }
  deletePost =() =>{
    this.api.deleteIntervention(this.selectedPost.id).subscribe(
      data => {
        this.getInterventions();

      },
      error => {
        console.log(error)
      }
    )
  }


  ngOnInit(): void {
  }

}
