import streamlit as st

import streamlit.components.v1 as components

st.title('HTML test')
st.title('Sign Up and Location Tracking')

# Simulate sign up
user_name = st.text_input("Enter your name")
user_email = st.text_input("Enter your email")

if st.button("Sign Up"):
    st.write(f"Welcome, {user_name}! You have successfully signed up.")

    HtmlFile = open('location.html', 'r', encoding='utf-8')

    source_code = HtmlFile.read()

    components.html(source_code,height=500)