import auth as au
import firebase_utils as fu
import os 

credentials_path = r"Syntax_Implementation\credentials.json"
uploaded_records_log = r"Syntax_Implementation\Logs\uploaded.txt"
fu.initialize_firebase()

# fu.upload_movies_to_firestore(uploaded_records_log)
# fu.get_movies_from_firestore()
# au.sign_up_user("ysooussef.a78@yahoo.com" , "zengy45")
# au.sign_in("ysooussef.a78@yahoo.com" , "zengy45")
# au.get_user_info("zeangy@yahoo.com" , "zengy45")
# au.send_password_reset_mail("ysoouef.a78@yahoo.com")
# au.sign_out_user("zeangy@yahoo.com" , "zengy45")