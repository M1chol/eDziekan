import handle_requests
import credentials
import handle_html
import os

if __name__ == "__main__":
    
    username, password = credentials.load()
    handle_requests.login(username, password)
    handle_html.convert()
    
    # Clean up temp files
    os.remove(handle_requests.target_name)
    os.remove(handle_html.temp_img_name)
    