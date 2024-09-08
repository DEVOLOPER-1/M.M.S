import streamlit as st
from streamlit_card import _streamlit_card
import auth as au_th

# def movie_card(movie_data):
    
    
    
    
    
# def cart_summary(cart_items): 
    
    
    
    
    
# def search_bar():
    
    
    
    
def main_page():
    st.title('Main Page')
    st.write(f'Welcome, {st.session_state.username}!')
    # st.button('Logout', on_click=logout)
    
    
    
def login_page():
    st.write("Welcome to the login page")
    username = st.text_input('Email')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        user_token = au_th.sign_in(user_mail=str(username) , user_pass=str(password))
        if user_token:
            st.session_state.authenticated = True
            return_of_user_info = au_th.get_user_info(user_token)
            st.session_state.username = return_of_user_info

            st.success('Login successful! Redirecting to the main page...')
            st.rerun(scope="app")  # Rerun the app to show the main page As the user will be authenyicated
    else:
        st.error('Invalid credentials. Please try again.' , icon="🚨")


def sign_up_page():
    st.title("Sign Up Page")
    email = st.text_input('Email')
    password = st.text_input('Choose a Password', type='password')
    if st.button("Sign Up"):
            if au_th.sign_up_user(email , password):
                st.success('Sign-up successful! You can now log in. , Redirecting to login Page...')
                st.session_state.page = 'login'
                # st.experimental_rerun()
                st.rerun(scope="app")
            else:
                st.error('Something Wen Wrong , Please Try to use another Email' , icon="🚨")
                

        
        
def reset_password_page():
    st.title('Reset Password Page')

    mail = st.text_input('Email')
    response = False
    if st.button('Reset Password'):
        if mail:
            response = au_th.send_password_reset_mail(mail)
            if response:
                st.success('Password reset link Was Sent To Your Email !')
                st.session_state.page = 'login'
                # st.experimental_rerun()
                st.rerun(scope="app")
            else:
                st.error("failed to send reset password link")    
        else:
            st.error("please enter a valid email address")

