import streamlit as st

add_selectbox = st.sidebar.selectbox("how would you like to conduct?",("mail","Mobile","Whatsup"))

with st.sidebar:
    add_radio = st.radio("Choose the shipping method",("Stanadrd (15-20 days)","Express(2-5 days"))
    name = st.text_input("Enter your name:")