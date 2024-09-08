import json
import requests
import os
from dotenv import load_dotenv
from firebase_admin import auth
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
load_dotenv(r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax Implementation\secrets.env")
api_key = os.getenv("web_api_key")
def verify_signed_up_email(link , registerer_email):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    my_mail = os.getenv("my_email")
    my_pass = os.getenv("email_pass")
    # my_mail.strip()
    # my_pass.strip()
    s.login(my_mail, my_pass)
    # create the email message
    msg = MIMEMultipart()
    msg['From'] = my_mail
    msg['To'] = registerer_email
    msg['Subject'] = "Verify Your Email Address With M.M.S"

    body = f"We're happy you signed up with us. Please verify your email by clicking the link: {link}"
    msg.attach(MIMEText(body, 'plain'))
    
    s.sendmail(my_mail, registerer_email, msg)
    # terminating the session
    s.quit()
    
    
def sign_up_user(email, password, user_name):
    user = auth.create_user(
        email=email,
        password=password
    )
    auth.update_user(user.uid, display_name=user_name)
    # link = auth.generate_email_verification_link(email=email)
    # verify_signed_up_email(link=link ,registerer_email=email)

def sign_in(user_mail , user_pass):

    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}'
    headers = {
        'Content-Type': 'application/json', #specifiying the content type of headers to json
    }
    payload = {
        'email': user_mail,
        'password': user_pass,
        'returnSecureToken': True
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("signed in successfully")
        data = response.json()
        print(data["registered"])
        idtoken = data["idToken"]
    else:
        data = response.json()
        print(data)
    return idtoken


def get_user_info(mail , passs):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={api_key}"
    headers = {
        'Content-Type': 'application/json', #specifiying the content type of headers to json
    }
    payload = {
            "idToken" : sign_in(mail , passs)
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    print(data)
    return data["localId"]

    
def send_password_reset_mail(user_mail):
    endpoint_url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}"
    headers = {
        'Content-Type': 'application/json', #specifiying the content type of headers to json
    }
    payload = {
            "requestType": "PASSWORD_RESET" ,
            "email" : user_mail
    }
    response = requests.post(endpoint_url, headers=headers, data=json.dumps(payload))
    data = response.json()
    print(data)
# def sign_out_user(user_mail , passs):
#     auth.revoke_refresh_tokens(uid=get_user_info(user_mail , passs))