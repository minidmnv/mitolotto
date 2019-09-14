import { Component, OnInit } from '@angular/core';
import {LoginService} from "./login.service";
import {Credentials} from "./credentials";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  errorMsg= '';
  loggedIn= '';

  constructor(private loginService: LoginService) {
  }

  ngOnInit(): void {

  }

  login(){
    console.log(this.loginService.credentials.username);
    console.log(this.loginService.credentials.password);
    this.errorMsg = 'Nie rozpoznano twarzy na zdjeciu';
    //this.loggedIn = 'Zalogowano'
    this.loginService.login();
  }

}
