import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from tqdm import tqdm
import datetime
import streamlit as st


# credentials_path = "credentials.json"
def initialize_firebase():
    credentials_path = r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax Implementation\credentials.json"
    cred = credentials.Certificate(credentials_path)
    firebase_admin.initialize_app(credential=cred)


def upload_movies_to_firestore(uploaded_records_file_path):
    try:
        db = firestore.client()
        """the name of the table is the argument of collection()
            the argument of document() is like an identifier to the record in the collection"""
            
        df = pd.read_csv(r"datasets\cleansed_prepared.csv", low_memory=False )

        df["vote_average"] = pd.to_numeric(df["vote_average"] ,errors= "coerce")
        df["popularity"] = pd.to_numeric(df["popularity"] ,errors= "coerce")
        df["adult"] = df["adult"].astype(bool , errors="ignore")
        df["release_date"] = pd.to_datetime(df["release_date"] , errors="coerce" , format="%Y-%m-%d")
        with open(uploaded_records_file_path , mode="r+") as uploaded_text_file:
            uploaded_ids = set(line.strip() for line in uploaded_text_file)

            for index , row in tqdm(df.iterrows() ,desc = "Uploading Data..." , total = len(df)):
                    if row["imdb_id"] in uploaded_ids:
                        continue
                    else:
                        doc_ref = db.collection('movies_table').document(str(row["imdb_id"]))
                        if pd.isna(row["release_date"]):
                            continue
                        doc_data = {
                        "imdb_id": row["imdb_id"],
                        "adult": row["adult"],
                        "collection": row["belongs_to_collection"],
                        "genres": row["genres"],
                        "homepage": row["homepage"],
                        "original_title": row["original_title"],
                        "overview": row["overview"],
                        "popularity": row["popularity"],
                        "poster_path": row["poster_path"],
                        "production_companies": row["production_companies"],
                        "production_countries": row["production_countries"],
                        "release_date": row["release_date"],  # .timestamp()
                        "spoken_languages": row["spoken_languages"],
                        "status": row["status"],
                        "tagline": row["tagline"],
                        "vote_average": row["vote_average"],
                        "idmb_url": row["idmb_url"],
                        "image_url": row["image_url"]
                        }
                        doc_ref.set(doc_data)
                        uploaded_text_file.write(f"{row['imdb_id']}\n")
                        uploaded_ids.add(row["imdb_id"])
    except Exception as e:
        print(f"An error occured: {e}")

    # temp_dict = df.to_dict(
    #     orient="records"
    # )  # returns a list of dictionaries ex: [{col_name:row_value},.......]

    
    # list(map(lambda x: doc_ref.add(x), temp_dict))
    # the map function is implemented in c , so it's faster than for loop significantly
    # the doc_ref.add(x) adds the record dictionary and in each iteration makes a new document with a new random reference

def get_movies_from_firestore():
    # initialize_firebase()
    db = firestore.client()
    movies_table_ref = db.collection("movies_table").limit(50)
    movies_metadata_lista = []

    for document in movies_table_ref.stream():
        
        output = document.to_dict()
        if output["imdb_id"] not in st.session_state.loaded_movies:
            st.session_state.loaded_movies.add(output["imdb_id"])
            movies_metadata_lista.append(output)
        else:
            continue
    return movies_metadata_lista


def add_movie_by_user(movie_id , movie_name  , adult , status):
    db = firestore.client()
    collection_ref = db.collection('movies_table')    
    doc_ref = collection_ref.document(str(movie_id))
    
    doc_data = {"imdb_id": str(movie_id),
                "adult": bool(adult),
                "collection": "N/A",
                "genres": "N/A",
                "homepage": "N/A",
                "original_title": str(movie_name),
                "overview": "N/A",
                "popularity": "N/A",
                "poster_path": "N/A",
                "production_companies": "N/A",
                "production_countries": "N/A",
                "release_date": "N/A",  # .timestamp()
                "spoken_languages": "N/A",
                "status": str(status),
                "tagline": "N/A",
                "vote_average": "N/A",
                "idmb_url": "N/A",
                "image_url": "N/A"}
    doc_ref.set(doc_data)
    
    
def update_movie_data(old_movie_id , movie_name, adult , status):
    db = firestore.client()
    collection_ref = db.collection('movies_table')    
    doc_ref = collection_ref.document(str(old_movie_id))
    
    doc_data = {"imdb_id": str(old_movie_id),
                "adult": bool(adult),
                "collection": "N/A",
                "genres": "N/A",
                "homepage": "N/A",
                "original_title": str(movie_name),
                "overview": "N/A",
                "popularity": "N/A",
                "poster_path": "N/A",
                "production_companies": "N/A",
                "production_countries": "N/A",
                "release_date": "N/A",  # .timestamp()
                "spoken_languages": "N/A",
                "status": str(status),
                "tagline": "N/A",
                "vote_average": "N/A",
                "idmb_url": "N/A",
                "image_url": "N/A"}
    doc_ref.update(doc_data)
    
    
def delete_movie(movie_id):
    db = firestore.client()
    collection_ref = db.collection('movies_table')
    collection_ref.document(str(movie_id)).delete()    
# def add_to_cart(user_id, movie_id):


# def get_user_cart(user_id):


# def checkout(user_id):
