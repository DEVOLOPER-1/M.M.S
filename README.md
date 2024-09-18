# 🎬 M.M.S - Movie Management System

Welcome to M.M.S, your ultimate movie management solution! 👋

## 📖 About the Project

M.M.S is a powerful and user-friendly application that allows you to manage and explore your movie collection like never before. Built with Streamlit and powered by Google Firebase, this project offers a seamless experience for movie enthusiasts and collectors alike.

### 🌟 Key Features

- 📚 Comprehensive movie library management
- 🔍 Advanced search and filtering options
- 📊 Popularity tracking and analytics
- 🛒 Shopping cart functionality
- 👤 User authentication and profiles
- 🔄 Real-time updates and synchronization

## 🚀 Getting Started

There are two ways to get M.M.S up and running on your local machine. Choose the method that works best for you!

### Method 1: Create Your Own Virtual Environment

1. Clone the repository:
'''
 git clone https://github.com/your-username/M.M.S.git 
   cd M.M.S
   '''
2. Create a virtual environment:
  '''
      python -m venv venv
   '''



3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
    '''
      pip install -r requirements.txt
   '''



5. Set up your Firebase configuration:
- Create a `firebase_config.json` file in the project root
- Add your Firebase project credentials to this file

6. Run the Streamlit app:
 '''
     streamlit run app.py

   '''



### Method 2: Use the Existing Virtual Environment

1. Clone the repository with the virtual environment:
  '''
   git clone --recursive https://github.com/your-username/M.M.S.git 
   cd M.M.S
   '''

2. Activate the existing virtual environment:
- On Windows:
  ```
  .venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source .venv/bin/activate
  ```

3. Set up your Firebase configuration:
- Create a `firebase_config.json` file in the project root
- Add your Firebase project credentials to this file

4. Run the Streamlit app:
  '''
      streamlit run main.py
   '''



## 🔧 Configuration

To connect M.M.S to your Firebase project:

1. Go to the Firebase Console and create a new project
2. Set up Authentication and Firestore Database
3. Generate a new private key for your service account
4. Save the private key as `firebase_config.json` in the project root

## 📘 Usage

After launching the app:

1. Sign up or log in to your account
2. Browse the movie library or search for specific titles
3. Add movies to your cart or update movie metadata
4. Explore popularity rankings and user stats
5. Enjoy managing your movie collection!

## 🤝 Contributing

We welcome contributions to M.M.S! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

Have questions or want to connect? Reach out to me on LinkedIn!

[Connect with me on LinkedIn](https://www.linkedin.com/in/your-profile/)

---

Happy movie managing! 🍿✨

