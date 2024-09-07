import firebase_utils as fu
import os 

credentials_path = r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax Implementation\credentials.json"
uploaded_records_log = r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax Implementation\Logs\uploaded.txt"
fu.initialize_firebase(credentials_path)

fu.upload_movies_to_firestore(uploaded_records_log)
