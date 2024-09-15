import streamlit as st
import auth as au_th
import firebase_utils as fu
import requests
from PIL import Image
from io import BytesIO
import random
import string
    




def movie_card(user_choice):
    if user_choice == "Movies Library":
        movie_data = fu.get_movies_from_firestore()
        
    if user_choice == "Cart":
        movie_data = fu.get_user_cart()[0]
    # Create columns
    cols = st.columns(1, gap="small", vertical_alignment='center')

    for i, single_movie in enumerate(movie_data):
        # Fetch movie image
        response = requests.get(single_movie["image_url"]) 
        if response.status_code not in [200, 201]:
            image_path = r"V:\INTERNSHIP\Hackathon Project\Resources\no_image.jpg"
            image = Image.open(image_path)
        else:    
            image = Image.open(BytesIO(response.content))
        
        # Assign movie to a column
        col_index = i % 1   
        with cols[col_index]:
            with st.container(border=True):
                st.title(single_movie["original_title"])
                st.subheader(f"Tagline: {single_movie["tagline"]}")
                st.image(image)
                if user_choice == "Movies Library":
                    st.button(label="Add To Cart" ,key=f"add_to_cart_{i}" , use_container_width=True , on_click=fu.add_to_cart(movie_id=single_movie["imdb_id"]))
                if user_choice == "Cart":
                    st.button(label="Remove from cart" ,key=f"add_to_cart_{i}" , use_container_width=True , on_click=fu.remove_from_cart(movie_id=single_movie["imdb_id"]))

                with st.expander("More Details :point_down:"):
                    
                    st.markdown(f"""IDMB_id: {single_movie["imdb_id"]}\n
                        For Adults: {single_movie["adult"]}\n
                        Genres: {single_movie["genres"]}\n
                        HomePage: {single_movie["homepage"]}\n
                        Popularity: {single_movie["popularity"]}\n
                        Production Companies: {single_movie["production_companies"]}\n
                        Production Countries: {single_movie["production_countries"]}
                        Release Date: {single_movie["release_date"]}\n
                        Spoken Languages: {single_movie["spoken_languages"]}\n
                        Status: {single_movie["status"]}\n
                        Vote Average: {single_movie["vote_average"]}\n
                        IDMB URL: {single_movie["idmb_url"]}\n
                        IMAGE URL: {single_movie["image_url"]}\n
                        Overview: {single_movie["overview"]}\n
                        """)
                    



    
    
    
def checkout_message(price):
    st.warning(body=f"Purcahase Done By total of {price} and ur purchase id is")
    
    
    
    
def main_page():
    
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Movies Library", "Cart" , "Most Popular bet. users"])
    if choice == "Movies Library":
        st.title('Movies Library')
        st.subheader("Welcome :smile: :wave:!")
        movie_card(user_choice="Movies Library")
        # st.button('Logout', on_click=logout)
        # st.button("Diplay More Movies" ,key="Display More Movies", on_click=movie_card)
    if choice == "Cart":  
        st.title('Your Cart')
        st.subheader("Welcome :smile: :wave:!")
        movie_card(user_choice="Cart")
        cart_movies_count = st.session_state.cart_movies_count
        total = cart_movies_count*35
        st.write(f"Remaining Movies in The Cart:{cart_movies_count} and Their Price is {total} $")
        st.button(label="Click Here To Check Out" , on_click=checkout_message(total))



                
def login_page():
    st.title('Login Page')
    
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        if email and password:
            # Add debug print
            print(f"Attempting to log in user: {email}")
            
            return_of_sign_in = au_th.sign_in(email, password)
            token = return_of_sign_in[0]
            userid = return_of_sign_in[1]
            if token and userid:
                st.session_state.idToken = token
                st.session_state.user_id = userid

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

