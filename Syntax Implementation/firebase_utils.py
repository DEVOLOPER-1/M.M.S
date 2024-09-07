import firebase_admin
from firebase_admin import credentials , firestore
import pandas as pd 
from tqdm import tqdm 

# credentials_path = "credentials.json"
def initialize_firebase(credentials_path):
    cred = credentials.Certificate(credentials_path)
    firebase_admin.initialize_app(credential=cred)
    
def upload_movies_to_firestore():
    db = firestore.client()
    doc_ref = db.collection("movies_table") 
    """the name of the table is the argument of collection()
        the argument of document() is like an identifier to the record in the collection"""
        
    df = pd.read_csv(r"datasets\cleansed_prepared.csv" , low_memory=False)
    
    temp_dict = df.to_dict(orient="records") #returns a list of dictionaries ex: [{col_name:row_value},.......] 
    
    tqdm(list(map(lambda x: doc_ref.add(x), temp_dict)) , total=len(df)) #the map function is implemented in c , so it's faster than for loop significantly
                                                    #the doc_ref.add(x) adds the record dictionary and in each iteration makes a new document with a new random reference
    
    
# def get_movies_from_firestore():
    
    
    
    
    
# def add_to_cart(user_id, movie_id):
    
    
    
    
    
# def get_user_cart(user_id):
    
    
    
    


# def checkout(user_id):
    
    