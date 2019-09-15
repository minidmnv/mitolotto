import { Component, OnInit, ElementRef, ViewChild, Output } from '@angular/core';
import {LoginService} from "../login.service";

@Component({
  selector: 'app-photo',
  templateUrl: './photo.component.html',
  styleUrls: ['./photo.component.css']
})
export class PhotoComponent implements OnInit {


  @ViewChild('video', {static: true})
  public video: ElementRef;

  @ViewChild('canvas', {static: true})
  public canvas: ElementRef;

  public captures: any;


  public constructor(private loginService: LoginService) {

  }

  photoButton = false;

  checkAccessToCamera(){
    if(this.video.nativeElement.srcObject == null){
      return true;
    }else{
      return false;
    }
  }

  public ngOnInit() {
  }

  public getPhotoButton() {
    return this.photoButton;
  }

  public ngAfterViewInit() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
        this.video.nativeElement.srcObject = stream;
        this.video.nativeElement.play();
        this.photoButton = true;
      });
    } else {
      this.photoButton = false;
    }
  }

  public reload() {
    this.video.nativeElement.play();
  }

  public capture() {
    this.canvas.nativeElement.getContext("2d").drawImage(this.video.nativeElement, 0, 0, 200, 200);
    this.captures = this.canvas.nativeElement.toDataURL("image/png");
    this.loginService.credentials.image = this.captures;
    this.video.nativeElement.pause();
  }


}
