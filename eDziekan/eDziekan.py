import requests

# Function to find end of html block
def crawl(text : str, index : int):
    while (text[index] != "<") and (text[index]!= ">"):
        index+=1
        char = text[index]
    return index

# Define the main URL
request_base = "https://s1.wcy.wat.edu.pl/ed1/index.php?"

# Define target - miniD
target_url = "https://s1.wcy.wat.edu.pl/ed1/logged.php?sid=61f672cfe47e00bae5151601edc47591&mid=450&iid=1&vrf=!82&pos=0"

# Define the payload data
payload = {
    "formname": "login",
    "userid": username,
    "password": password,
    "default_fun": "1",
}
# Headers to mimic real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}
requests.packages.urllib3.disable_warnings()

# Send the POST request
with requests.Session() as session:
    
    main_site = session.get(request_base, verify=False)
    if main_site.status_code == 200:
        print("main_site request successful")
        if "sid=" in main_site.text: print("locating sid")
        sid_index=main_site.text.index("sid=")
        login_sid=main_site.text[sid_index:crawl(main_site.text, sid_index)]
        print(login_sid, "\nTrying to log in...")
    
        tryLogin = session.post(request_base+login_sid, data=payload, headers=headers, verify=False)
    
        if tryLogin.status_code == 200:
            print("Login successful")
            with open("response.html", "w", encoding="utf-8") as file:
                file.write(tryLogin.text)
        else: print("Login failed")

