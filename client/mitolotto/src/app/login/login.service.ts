import { HttpClient, HttpHeaders} from '@angular/common/http';

const endpoint = 'http://localhost:3000/api/v1/';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};


export class LoginService {
  constructor(private http: HttpClient) { }

}
