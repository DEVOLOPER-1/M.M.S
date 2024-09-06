import firebase_admin
from firebase_admin import credentials

credentials_path = "credentials.json"
def initialize_firebase(credentials_path):
    cred = credentials.Certificate(credentials_path)
    firebase_admin.initialize_app(credential=cred , 
                                )
    
    
    
def get_movies_from_firestore():
    
    
    
    
    
def add_to_cart(user_id, movie_id):
    
    
    
    
    
def get_user_cart(user_id):
    
    
    
    


def checkout(user_id):
    
    