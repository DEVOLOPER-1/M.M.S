import json

def sign_in_user(email, password , credentials_path):
    # cred = credentials.Certificate(credentials_path)
    # firebase = firebase_admin.initialize_app(credential=cred)
    with open("credentials.json" , "r") as cred_file:
        cred = json.load(cred_file)
    firebase = pyrebase.initialize_app(cred)
    auth = firebase.auth()
    
    
    
    
# def sign_up_user(email, password):


# def get_current_user():

# def sign_out_user():