import { Component, OnInit, ElementRef, ViewChild, Output } from '@angular/core';
import { EventEmitter } from 'events';

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

  

  public constructor() {

  }
  photoButton = false;

  public ngOnInit() { }

  public getPhotoButton(){
    return this.photoButton;
  } 

  public ngAfterViewInit() {
      if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
              this.video.nativeElement.srcObject = stream;
              this.video.nativeElement.play();
              this.photoButton = true;
          });
      }
      else{
        this.photoButton = false;
      }
  }

  public reload(){
    console.log("show button, jaki jest: "+this.photoButton );
    this.video.nativeElement.play();
  }

  public capture() {
    console.log("sassasasas");
      var context = this.canvas.nativeElement.getContext("2d").drawImage(this.video.nativeElement, 0 ,0 , 200, 200);
      this.captures = this.canvas.nativeElement.toDataURL("image/png");
      this.video.nativeElement.pause();

  }



  //  @ViewChild('videoElement', {static: true}) videoElement: any;
  // video: any;

  // isPlaying = false;

  // displayControls = true;

  // ngOnInit() {
  //   this.video = this.videoElement.nativeElement;
  // }

  // start() {
  //   this.initCamera({ video: true, audio: false });
  // }

  // pause() {
  //   this.video.pause();
  // }

  // toggleControls() {
  //   this.video.controls = this.displayControls;
  //   this.displayControls = !this.displayControls;
  // }

  // resume() {
  //   this.video.play();
  // }

  // sound() {
  //   this.initCamera({ video: true, audio: true });
  // }

  // initCamera(config:any) {
  //   var browser = <any>navigator;

  //   browser.getUserMedia = (browser.getUserMedia ||
  //     browser.webkitGetUserMedia ||
  //     browser.mozGetUserMedia ||
  //     browser.msGetUserMedia);

  //   browser.mediaDevices.getUserMedia(config).then(stream => {
  //     this.video.src = window.URL.createObjectURL(stream);
  //     this.video.play();
  //   });
  // }

}
