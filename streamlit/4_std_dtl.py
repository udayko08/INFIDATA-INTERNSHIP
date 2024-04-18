import streamlit as st

name = st.text_input("Enter your name:")
reg = st.text_input("Enter your regNo:")
course = st.text_input("Enter your course:")
email = st.text_input("Enter your mail id:")

test1 = st.number_input("Enter your Test1 marks:")
test2 = st.number_input("Enter your test2 marks:")
test3 = st.number_input("Enter your test3 marks:")

avg = (test1+test2+test3)/3

st.write("The average marks of test 1,2,3  is",avg)
st.write("student name:",name)
st.write("Student reg:",reg)
st.write("student course:",course)
st.write("Student email:",email)