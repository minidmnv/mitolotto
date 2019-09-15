import { Component, OnInit } from '@angular/core';
import {LoginService} from "./login.service";
import {CredentialsResponse} from "./credentialsResponse";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  errorMsg= '';
  loggedIn= '';

  constructor(public loginService: LoginService) {
  }

  ngOnInit(): void {

  }

  login(){
    console.log(this.loginService.credentials.username);
    console.log(this.loginService.credentials.password);
    this.errorMsg = '';
    this.loggedIn = '';
    this.loginService.login().subscribe(
      response => {
        console.log(response.details);
        if(response.authorized == 'True'){
          this.loggedIn = response.details;
        }
        else{
          this.errorMsg = response.details;
        }
      }
    )
  }

}
