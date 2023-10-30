import requests

# Function to find end of html block
def crawl(text : str, index : int):
    while (text[index] != "<") and (text[index]!= ">"):
        index+=1
        char = text[index]
    return index

# Define the main URL
request_base = "https://s1.wcy.wat.edu.pl/ed1/index.php?"

# Headers to mimic real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Define target html name
target_name = "response.html"

def login(username, password):
    # Define the payload data
    payload = {
        "formname": "login",
        "userid": username,
        "password": password,
        "default_fun": "1",
    }
    # Block verification - not sure if needed
    requests.packages.urllib3.disable_warnings()
    with requests.Session() as session:
        # Send the POST request to main edziekanat site
        try:
            main_site = session.get(request_base, verify=False)
        except requests.ConnectTimeout:
            print("Connection timeout, aborting...")
            quit()
        except requests.ConnectionError:
            print("Not connected to internet, aborting...")
            quit()
        if main_site.status_code == 200:
            print("main_site request successful")
            # Locate Session ID - needed to create proper login request
            if "sid=" in main_site.text: print("locating sid")
            sid_index=main_site.text.index("sid=")
            login_sid=main_site.text[sid_index:crawl(main_site.text, sid_index)]
            print(login_sid, "\nTrying to log in...")
            # Sending login request
            tryLogin = session.post(request_base+login_sid, data=payload, headers=headers, verify=False)
            if tryLogin.status_code == 200:
                print("Login successful")
                # Save site as html for later processing
                with open(target_name, "w", encoding="iso-8859-2") as file:
                    file.write(tryLogin.text)
            else: print("Login failed")

