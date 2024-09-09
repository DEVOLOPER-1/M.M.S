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
    st.title('Login Page')
    
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        if email and password:
            # Add debug print
            print(f"Attempting to log in user: {email}")
            
            success = au_th.sign_in(email, password)
            return_of_user_info = au_th.get_user_info(success)
            if success:
                st.session_state.username = return_of_user_info
                st.success('Logged in successfully!')
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error('Invalid email or password. Please try again.')
        else:
            st.error('Please enter both email and password.')


        
        
def sign_up_page():
    st.title('Sign Up Page')
    
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    if st.button('Sign Up'):
        if email and password:
            
            success = au_th.sign_up_user(email=str(email), password=str(password))
            
            if success:
                st.success('Account created successfully!')
                st.session_state.page = 'login'
                st.rerun()
            else:
                st.error('Failed to create account. Please try again.')
        else:
            st.error('Please fill in all fields.')






def reset_password_page():
    st.title('Reset Password Page')
    
    mail = st.text_input('Email')
    
    if st.button('Reset Password'):
        if mail:
            print(f"Attempting to reset password for email: {mail}")
            
            response = au_th.send_password_reset_mail(user_mail=str(mail))
            
            if response:
                st.success('Password reset link was sent to your email!')
                st.session_state.page = 'login'
                st.rerun()
            else:
                st.error('Failed to send password reset link. Please try again.')
        else:
            st.error('Please enter a valid email address.')

