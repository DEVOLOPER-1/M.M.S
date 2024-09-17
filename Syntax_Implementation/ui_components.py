import streamlit as st
import auth as au_th
import firebase_utils as fu
import requests
from PIL import Image
from io import BytesIO
import random
import string
import pandas as pd


def movie_card(user_choice):
    # Fetch movie data
    if user_choice == "Movies Library":
        movie_data = st.session_state.movies_metadata_lista
    elif user_choice == "Cart":
        movie_data = st.session_state.user_purchases

    # Create columns (e.g., 3 columns for the movie cards)
    cols = st.columns(1)

    for i, single_movie in enumerate(movie_data):
        # Fetch movie image
        try:
            response = requests.get(single_movie["image_url"])
            if response.status_code in [200, 201]:
                image = Image.open(BytesIO(response.content))

            else:
                image = None
                image_path = r"V:\INTERNSHIP\Hackathon Project\Resources\no_image.jpg"
                image = Image.open(image_path)
        except:
            print("retreiving image error")
            image_path = r"V:\INTERNSHIP\Hackathon Project\Resources\no_image.jpg"
            image = Image.open(image_path)
        # Assign movie to a column
        col_index = i % 3  # Change 3 to however many columns you want
        with cols[0]:
            with st.container():
                st.title(single_movie["original_title"])
                st.subheader(f"Tagline: {single_movie['tagline']}")
                st.image(image)
                movie_id = single_movie["imdb_id"]

                if user_choice == "Movies Library":
                    st.button(
                        label="Add To Cart",
                        key=f"add_to_cart_{i}",
                        use_container_width=True,
                        on_click=fu.add_to_cart,
                        args=(single_movie["imdb_id"],),
                    )

                    with st.expander("More Details :point_down:"):
                        st.markdown(
                            f"""
                        IMDB ID: {single_movie['imdb_id']}\n
                        For Adults: {single_movie['adult']}\n
                        Genres: {single_movie['genres']}\n
                        HomePage: {single_movie['homepage']}\n
                        Popularity: {single_movie['popularity']}\n
                        Production Companies: {single_movie['production_companies']}\n
                        Production Countries: {single_movie['production_countries']}\n
                        Release Date: {single_movie['release_date']}\n
                        Spoken Languages: {single_movie['spoken_languages']}\n
                        Status: {single_movie['status']}\n
                        Vote Average: {single_movie['vote_average']}\n
                        IMDB URL: {single_movie['idmb_url']}\n
                        Overview: {single_movie['overview']}\n
                        """
                        )
                    with st.expander("Update Movie Metadata"):
                        with st.form(f"update_movie_{movie_id}"):
                            genres = st.text_input(
                                label="Enter Genres", key=f"genres_{movie_id}"
                            )
                            idmb_url = st.text_input(
                                label="Enter IDMB URL", key=f"idmb_url_{movie_id}"
                            )
                            image_url = st.text_input(
                                label="Enter Image URL", key=f"img_url_{movie_id}"
                            )
                            home_page = st.text_input(
                                label="Enter HOMEPAGE URL", key=f"hm_page_{movie_id}"
                            )

                            new_data_dict = {
                                "genres": genres,
                                "idmb_url": idmb_url,
                                "image_url": image_url,
                                "homepage": home_page,
                            }
                            form_submit_button = st.form_submit_button(
                                "Send The New MetaData", use_container_width=True
                            )
                            if form_submit_button:
                                fu.update_movie_data(
                                    movie_id=movie_id, new_data_dict=new_data_dict
                                )
                                st.toast("Data Sent and Updated")
                elif user_choice == "Cart":
                    st.button(
                        label="Remove from Cart",
                        key=f"remove_from_cart_{i}",
                        use_container_width=True,
                        on_click=fu.remove_from_cart,
                        args=(single_movie["imdb_id"],),
                    )


def checkout_message(price):
    characters_and_digits = string.ascii_letters + string.digits
    purchase_id = ""
    i = 0
    for i in range(10):
        purchase_id += "".join(random.choice(characters_and_digits))
        i += 1
    st.success(
        body=f"Purcahase Done By total of {price} $$ and ur purchase id is **{purchase_id}** !!",
        icon="💸",
    )


# def display_user_info():
#     st.


def main_page():

    st.sidebar.title("Navigation")
    choice = st.sidebar.radio(
        "Go to", ["Movies Library", "Cart", "Most Popular bet. users", "Update My Info"]
    )
    if choice == "Movies Library":
        fu.get_movies_from_firestore()
        st.title("Movies Library")
        st.subheader("Welcome :smile: :wave:!")
        movie_card(user_choice="Movies Library")
        # st.button('Logout', on_click=logout)
        # st.button("Diplay More Movies" ,key="Display More Movies", on_click=movie_card)
    if choice == "Cart":
        fu.get_user_cart()
        st.title("Your Cart")
        st.subheader("Welcome :smile: :wave:!")
        cart_movies_count = int(st.session_state.cart_movies_count)
        total = cart_movies_count * 35
        count_col, price_col = st.columns(2, gap="large")
        with count_col:
            st.metric(label="Remaining Movies in The Cart 🛒", value=cart_movies_count)
        with price_col:
            st.metric(label="Total Price 💸💸", value=total)
        movie_card(user_choice="Cart")
        checkout_button = st.button(label="Click Here To Check Out")
        if checkout_button and total > 0:
            checkout_message(total)

        # st.button(label="Click Here To Check Out" , on_click=checkout_message(total))

    if choice == "Most Popular bet. users":
        st.title("Most Popular Movies bet. users")
        st.subheader("Welcome :smile: :wave:!")

        data = fu.calculate_popularity()
        df = pd.DataFrame(data=data)
        col1, col2, col3 = st.columns(3)
        with col3:
            sort_table_toggle = st.toggle("Sorted Dataframe")
        st.table(data=df)
        if sort_table_toggle:
            df_sorted = df.sort_values(by="popularity_index", ascending=False)
            st.table(df_sorted)

    if choice == "Update My Info":
        st.title("User Info ℹ️")
        st.subheader("Have a look on ur info before updating it 👀😄")
        # col1, col2 = st.columns(2, gap="small")

        with st.container(border=True):
            token = st.session_state.idToken
            user_info = au_th.get_user_info(token=token)

            st.markdown(
                f"""
                ### 👤 User Profile

                📧 **Email:** 
                {user_info['users'][0]['email']}
                
                🏷️ **User name:** 
                {user_info['users'][0]['providerUserInfo'][0]['displayName']}
                
                🖼️ **Photo Url:** 
                {user_info['users'][0]['providerUserInfo'][0]['photoUrl']}
                
                🕒 **Last Refresh:** 
                {user_info['users'][0]['lastRefreshAt'][:10]}
                
                ✅ **Verified Email:** 
                {'Yes ✔️' if user_info['users'][0]['emailVerified'] else 'No ❌'}
                """
            )
            with st.expander("Update Info"):
                with st.form(f"Update Personal Data Form", clear_on_submit=True):
                    user_name = st.text_input(label="Enter New User name")
                    photo_url = st.text_input(label="Enter Personal Photo Url")

                    new_data_dict = {
                        "idToken": str(st.session_state.idToken),
                        "displayName": str(user_name),
                        "photoUrl": str(photo_url),
                        "returnSecureToken": True,
                    }
                    submit_button = st.form_submit_button(
                        "Submit New Data",
                        use_container_width=True,
                        on_click=au_th.update_user_info,
                        args=(new_data_dict,),
                    )
                    if submit_button:
                        st.success("Sent Successfully")
                        st.balloons()


def login_page():
    st.title("Login Page")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email and password:
            # Add debug print
            print(f"Attempting to log in user: {email}")

            return_of_sign_in = au_th.sign_in(email, password)
            token = return_of_sign_in[0]
            userid = return_of_sign_in[1]
            if token and userid:
                st.session_state.idToken = token
                st.session_state.user_id = userid

                st.toast("Logged in successfully!")
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid email or password. Please try again.")
        else:
            st.error("Please enter both email and password.")


def sign_up_page():
    st.title("Sign Up Page")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if email and password:

            success = au_th.sign_up_user(email=str(email), password=str(password))

            if success:
                st.toast("Account created successfully!")
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error("Failed to create account. Please try again.")
        else:
            st.error("Please fill in all fields.")


def reset_password_page():
    st.title("Reset Password Page")

    mail = st.text_input("Email")

    if st.button("Reset Password"):
        if mail:
            print(f"Attempting to reset password for email: {mail}")

            response = au_th.send_password_reset_mail(user_mail=str(mail))

            if response:
                st.toast("Password reset link was sent to your email!")
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error("Failed to send password reset link. Please try again.")
        else:
            st.error("Please enter a valid email address.")
