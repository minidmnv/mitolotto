import { HttpClient, HttpHeaders} from '@angular/common/http';
import {Credentials} from "./credentials";

const endpoint = 'http://localhost:3000/api/v1/';
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

}
