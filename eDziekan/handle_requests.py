import requests

# Define the main URL
request_base = "https://s1.wcy.wat.edu.pl/ed1/index.php?"

# Headers to mimic real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Define target html name
target_name = "response.html"

class edziekanSession:
    def __init__(self) -> None:
        self.requestBase = request_base
        self.headers = headers
        self.targetHtmlName = target_name
        self.sid = ""
        self.session = requests.Session()
        self.log = False
        self.username = ""
        self.password = ""
    
    def Init(self, log=False) -> None:
        self.log = log
        # disable wornings for ssl certification
        requests.packages.urllib3.disable_warnings()
        # Send the POST request to main edziekanat site
        try:
            main_site = self.session.get(self.requestBase, verify=False)
        except requests.ConnectTimeout:
            self.Log("Connection timeout, aborting...")
            self.Abort(-2)
        except requests.ConnectionError:
            self.Log("Not connected to internet, aborting...")
            self.Abort(-2)
        if main_site.status_code == 200:
            self.Log("main_site request successful")
            # Locate Session ID - needed to create proper login request
            if "sid=" in main_site.text: self.Log("extracting sid...")
            else: 
                self.Log('failed locating sid, aborting...')
                self.Abort(-1)
            sid_index=main_site.text.index("sid=")
            self.sid=main_site.text[sid_index:sid_index+36]
        
    def Abort(self, errorCode) -> int:
        print(f"Session exited with status: {errorCode},")
        if errorCode == -2: print("You are probably not connected to network or edziekanat is down")
        if errorCode == -1: print("One or more processes of app failed or edziekanat was updated, please contact creator")
        return errorCode
        
    def Log(self, logMessege) -> None:
        if self.log: print(logMessege)
        

    def Login(self):
        # Define the payload data
        payload = {
            "formname": "login",
            "userid": self.username,
            "password": self.password,
            "default_fun": "1",
        }
        self.Log(f"{self.sid}\nTrying to log in...")
        # Sending login request
        #try:
        tryLogin = self.session.post(self.requestBase+self.sid, data=payload, headers=self.headers, verify=False)
        #except:
        #self.Log('error occured while posting login info')
        #self.Abort(-2)
        if tryLogin.status_code == 200:
            self.Log("Login successful")
        else: 
            self.Log("Login returned wrong status code")
            self.Abort(-2)
           
    def requestScheduleTxt(self) -> None:
        self.Log("requesting schedule")
        
        adress='https://s1.wcy.wat.edu.pl/ed1/logged_inc.php?'+self.sid+'&mid=328&iid=20234&exv=WCY23KY2S1&pos=0&rdo=1&t=6801839'
        resp = requests.get(adress, headers=self.headers, verify=False, allow_redirects=True)
        
        filename = 'downloaded_file.html'

        if resp.status_code == 200:
            self.Log('file located')    
            with open(filename, 'wb') as file:
                file.write(resp.content)
        else:
            self.Log('file not found')
            
    def loadCredentials(self, username, password):
        self.username = username
        self.password = password


