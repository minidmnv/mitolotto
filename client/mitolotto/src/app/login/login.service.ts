import { HttpClient, HttpHeaders} from '@angular/common/http';
import {Credentials} from "./credentials";
import {CredentialsResponse} from "./credentialsResponse";
import {Observable} from "rxjs";

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

  login(): Observable<any>{
    console.log(this.credentials);
    return this.http.post(endpoint,this.credentials, httpOptions);
  }

}
