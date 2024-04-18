import datetime

import streamlit as st

st.header("Student Registration Form")

my_form = st.form(key = "form-1")
f_name = my_form.text_input("Enter your First_name")
l_name = my_form.text_input("Enter your Last_name")
email = my_form.text_input("Enter your mail id")
mobile = my_form.text_input("Enter your number")
gender = my_form.radio('Gender',('male','female'))
age = my_form.slider('Age',1,100)
dob = my_form.date_input("Enter date of birth",min_value=datetime.date(1990,1,1))
address = my_form.text_area("Enter your Address")
resume = my_form.file_uploader("Upload your resume")
my_form.form_submit_button("Submit")

st.write("First_name",f_name)
st.write("Last_name",l_name)
st.write("Email",email)
st.write("Mobile number",mobile)
st.write("Gender",gender)
st.write("Age",age)
st.write("Date of birth",dob)
st.write("Address",address)