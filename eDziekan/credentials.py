import os

# IMPORTANT - if you ever change the name of file containing password remember to add it to gitignore
passFile = "hasla.txt" 

def load():
    if os.path.exists(passFile):
        print("Loading credentials")
        with open(passFile, 'r') as dane:
            username, password = dane.readline().split()
        print("Using credentials of", username)
    else:
        print("IMPORTANT - Remember that your password and username is stored locally without encription. Anyone can gain acces to this file:",passFile)
        username = input("Input username: ")
        password = input("Input password: ")
        with open(passFile, 'w') as dane:
            print(username, password, file=dane)
    return username, password