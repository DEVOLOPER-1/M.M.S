import auth as au
import firebase_utils as fu
import os 

credentials_path = r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax Implementation\credentials.json"
uploaded_records_log = r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax Implementation\Logs\uploaded.txt"
fu.initialize_firebase(credentials_path)

# fu.upload_movies_to_firestore(uploaded_records_log)
# fu.get_movies_from_firestore()
# au.sign_up_user("youssef.a78@yahoo.com" , "zengy45","xy")
# au.sign_in("zengy@yahoo.com" , "zengy45")
# au.get_user_info("zeangy@yahoo.com" , "zengy45")
# au.send_password_reset_mail("youssef.a78@yahoo.com")
au.sign_out_user("zeangy@yahoo.com" , "zengy45")