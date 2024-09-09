import streamlit as st
from streamlit_card import card
import auth as au_th
import firebase_utils as fu


# def movie_card():
#     movie_data = fu.get_movies_from_firestore()
#     for single_movie in movie_data:
        
#         hasClicked = card(
#         title=single_movie["original_title"],
#         text=single_movie["tagline"],
#         image=single_movie["image_url"],
#         url=single_movie["idmb_url"]
# )
    


def movie_card():
    movie_data = fu.get_movies_from_firestore()
    for single_movie in movie_data:
        hasClicked = card(
            title=single_movie["original_title"],
            text=single_movie["tagline"],
            image=single_movie["image_url"],
            url=single_movie["idmb_url"]
        )
        
        # Add an expander for additional movie details
        # with st.expander("See more details"):
        #     st.write(f"Release Date: {single_movie.get('release_date', 'N/A')}")
        #     st.write(f"Runtime: {single_movie.get('runtime', 'N/A')} minutes")
        #     st.write(f"Overview: {single_movie.get('overview', 'N/A')}")
            # Add more details as needed
        
        # You can use the hasClicked variable to perform actions when the card is clicked
        if hasClicked:
            st.write(f"You clicked on {single_movie['original_title']}")    
    
# def cart_summary(cart_items): 
    
    
    
    
    
# def search_bar():
    
    
    
    
def main_page():
    st.title('Main Page')
    st.write(f'Welcome, {st.session_state.username}!')
    movie_card()
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

