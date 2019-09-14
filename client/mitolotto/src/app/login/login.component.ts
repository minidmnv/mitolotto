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

  credentials: Credentials;

  constructor(private loginService: LoginService) {
  }

  ngOnInit(): void {
    this.credentials = new Credentials();
  }

  login(){
    console.log(this.credentials.login);
    console.log(this.credentials.password);
    //this.errorMsg = 'Nie rozpoznano twarzy na zdjeciu';
    this.loggedIn = 'Zalogowano'
  }

}
