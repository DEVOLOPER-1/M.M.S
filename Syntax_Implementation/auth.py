import json
import requests
import os
from dotenv import load_dotenv
import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv(r"V:\INTERNSHIP\Hackathon Project\M.M.S\Syntax_Implementation\secrets.env")
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
    
    
def sign_up_user(email, password):
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}'
    headers = {
        'Content-Type': 'application/json', #specifiying the content type of headers to json
    }
    payload = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    if response.status_code == 200:
        return True


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
    data = response.json()
    print(data)
    if response.status_code == 200:
        return [data["idToken"],data['localId']]
    


def get_user_info(token):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={api_key}"
    headers = {
        'Content-Type': 'application/json', #specifiying the content type of headers to json
    }
    payload = {
            "idToken" : st.session_state.idToken
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    print(data)
    # return data["displayName"]

    
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
    if response.status_code == 200:
        return True
    else:
        return False

def update_user_info(new_user_name , user_photo_url):
    idToken = st.session_state.idToken
    endpoint_url = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={api_key}"
    headers = {
        'Content-Type': 'application/json', #specifiying the content type of headers to json
    }
    payload = {
    "idToken": str(idToken),
    "displayName": str(new_user_name),
    "photoUrl": str(user_photo_url),
    "returnSecureToken": True
}
    response = requests.post(endpoint_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return True
    else:
        return False


# def sign_out_user(user_mail , passs):
#     auth.revoke_refresh_tokens(uid=get_user_info(user_mail , passs))