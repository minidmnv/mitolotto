import { HttpClient, HttpHeaders} from '@angular/common/http';
import {Credentials} from "./credentials";

const endpoint = 'http://localhost:5000/authorize';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};


export class LoginService {

  credentials: Credentials;


  constructor(private http: HttpClient) {
    this.credentials = new Credentials();
  }

  login(){
    console.log(this.credentials);
    this.http.post(endpoint,this.credentials, httpOptions).subscribe();
  }

}
