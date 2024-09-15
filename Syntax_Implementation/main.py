import streamlit as st
import ui_components as ui
import firebase_utils as fu

# Main app logic


def main():
    
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "page" not in st.session_state:
        st.session_state.page = "login"
        
    if "loaded_movies" not in st.session_state:
        st.session_state.loaded_movies = set()
    
    if "idToken" not in st.session_state:
        st.session_state.idToken = None
        
    if "user_id"not in st.session_state:
        st.session_state.user_id = None
    if "cart_movies_count" not in st.session_state:
        st.session_state.cart_movies_count = None
    if st.session_state.authenticated:
        ui.main_page()
    
        
    # if "initialize_firebase" not in st.session_state:
    #         st.session_state.initialize_firebase = False
            
    # if st.session_state.initialize_firebase == False:
    #     fu.initialize_firebase()
    #     st.session_state.initialize_firebase = True
        
    else:
        st.sidebar.title("Navigation")
        choice = st.sidebar.radio("Go to", ["Login", "Sign Up", "Reset Password"])

        if choice == "Login":
            st.session_state.page = "login"
        elif choice == "Sign Up":
            st.session_state.page = "sign_up"
        elif choice == "Reset Password":
            st.session_state.page = "reset_password"

        if st.session_state.page == "login":
            ui.login_page()
        elif st.session_state.page == "sign_up":
            ui.sign_up_page()
        elif st.session_state.page == "reset_password":
            ui.reset_password_page()


if __name__ == "__main__":
    main()
