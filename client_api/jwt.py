from dataclasses import dataclass
import requests
from getpass import getpass
import pathlib
import json

@dataclass
class JwtClient:
    """
    user a dataclass decorator
    to simply the class construction
    """
    access:str = None
    refresh:str = None
    #ensure this matches your simplejwt config
    header_type:str = "Bearer"
    #this assumesy ou have DRF running on localhost:8000
    base_endpoint = "http://localhost:8000/api"
    #this file path is insecure
    cred_path: pathlib.Path = pathlib.Path("creds.json")
    def __post_init__(self):
        if self.cred_path.exists():
            """
            you have stored creds,
            let's verify them
            and refresh them.
            if that fails,
            restart login process.
            """
            try:
                data = json.loads(self.cred_path.read_text())
            except Exception:
                print("Assuming creds has been tampered with")
                data = None
            if data is None:
                """
                Clear stored creds and
                Run login process
                """
                self.clear_tokens()
                self.perform_auth()
            else:
                """
                creds.json was not tampered with
                Verify token -&gt;
                if necessary, refresh token -&gt;
                if necessary, Run login process
                """
                self.access = data.get('access')
                self.refresh = data.get('refresh')
                token_verified = self.verify_token()
                if not token_verified:
                    """
                    this can mean the token has expired
                    or is invalid. Either way, attempt a refresh.
                    """
                    refreshed = self.perform_refresh()
                    if not refreshed:
                        """
                        this means the token refresh 
                        olso failed. Run login process
                        """
                        print("invalid data, login again.")
                        self.clear_tokens()
                        self.perform_auth()
        else:
            """
            Run login process
            """
            self.perform_auth()
    
    def get_headers(self, header_type=None):
        _type = header_type or self.header_type
        token = self.access
        if not token:
            return {}
        return {
            "Authorization":f"{_type} {token}"
        }
    
    def perform_auth(self):
        endpoint = f"{self.base_endpoint}/token/"
        print(endpoint)
        username = input("what is your username?\n")
        password = getpass("what is your password?\n")
        r = requests.post(endpoint, json={'username':username, 'password': password})
        if r.status_code != 200:
            raise Exception(f"Access not granted: {r.text}")
        print('access granted')
        self.write_creds(r.json())
    
    def write_creds(self, data:dict):
        
        if self.cred_path is not None:
            self.access = data.get('access')
            self.refresh = data.get("refresh")
            if self.access and self.refresh:
                self.cred_path.write_text(json.dumps(data))
    
    def verify_token(self):
        data = {
            "token": f"{self.access}"
        }
        endpoint = f"{self.base_endpoint}/token/verify"
        r = requests.post(endpoint, json=data)
        return r.status_code == 200
    
    def clear_tokens(self):
        self.access = None
        self.refresh = None
        if self.cred_path.exists():
            self.cred_path.unlink()
    
    def perform_refresh(self):
        print("Refreshing token.")
        headers = self.get_headers()
        data = {
            "refresh":f"{self.refresh}"
        }
        endpoint = f"{self.base_endpoint}/token/refresh/"
        r = requests.post(endpoint, json=data, headers=headers)
        if r.status_code != 200:
            self.clear_tokens()
            return False
        refresh_data = r.json()
        if not 'access' in refresh_data:
            self.clear_tokens()
            return False
        stored_data = {  
            'access':refresh_data.get('access'),
            'refresh':self.refresh
        }
        self.write_creds(stored_data)
        return True
    
    def list(self, endpoint=None, limit=3):
        headers = self.get_headers()
        if endpoint is None or self.base_endpoint not in str(endpoint):
            endpoint = f"http://127.0.0.1:8000/product/create-list?limit={limit}"
        r = requests.get(endpoint, headers=headers)
        if r.status_code != 200:
            raise Exception(f"Request not complete {r.text}")
        data = r.json()
        return data

if __name__=="__main__":
    client = JwtClient()
    lookup_1_data = client.list(limit=5)
    results = lookup_1_data.get('results')
    print(lookup_1_data)
    next_url = lookup_1_data.get('next')
    print("First lookup result length", len(results))
    if next_url:
        lookup_2_data = client.list(endpoint=next_url)
        results +=lookup_2_data.get('results')
        print("second lookup result length", len(results))