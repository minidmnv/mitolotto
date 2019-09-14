import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  errorMsg= '';

  constructor() { }

  ngOnInit() {
  }

  login(){
    this.errorMsg = 'Nie rozpoznano twarzy na zdjeciu';
  }

}