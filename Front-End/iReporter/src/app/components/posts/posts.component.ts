import { Component, OnInit } from '@angular/core';
import {PostsService} from "../../services/posts.service";

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css'],
  providers:[PostsService]
})
export class PostsComponent implements OnInit {
  posts = [{id:1},{url:'testurl'},{title:'test'}, {info:'test'},{location:'location'}, {image:'https://res.cloudinary.com/ireporter2022/image/upload/v1656953718/crime5_r8mbnm.jpg'}];
  selectedPost: any;

  constructor(private api: PostsService) {
    this.getRedFlags();
    this.selectedPost ={id:-1, title:'', info:'', location:'', }
  }
  getRedFlags=() =>{
    this.api.getAllRedFlags().subscribe(
      data => {
        this.posts =data
      },
      error => {
        console.log(error)
      }
    )
  }

  postClicked = (post:any)=>{
    this.api.getOneRedFlag(post.id).subscribe(
      data => {
        this.selectedPost = data;

      },
      error => {
        console.log(error)
      }
    )
  }


  updatePost =() =>{
    this.api.updateRedFlag(this.selectedPost).subscribe(
      data => {
        this.getRedFlags();

      },
      error => {
        console.log(error)
      }
    )
  }
  createPost =() =>{
    this.api.createRedFlag(this.selectedPost).subscribe(
      data => {
        this.getRedFlags();

      },
      error => {
        console.log(error)
      }
    )
  }
  deletePost =() =>{
    this.api.deleteRedFlag(this.selectedPost.id).subscribe(
      data => {
        this.getRedFlags();

      },
      error => {
        console.log(error)
      }
    )
  }


  ngOnInit(): void {

  }



}
