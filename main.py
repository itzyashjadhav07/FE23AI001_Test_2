import streamlit as st

email = st.text_input('Enter email - ')
password = st.text_input('Enter Password - ')
btn = st.button('Login')

if btn:
    if email == 'amangupta@gmail.com' and password == '12345':
        st.balloons()
        st.success("Logged In ")

    else:
        st.error('Login Failed')