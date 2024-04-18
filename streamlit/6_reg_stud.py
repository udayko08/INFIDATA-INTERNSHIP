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
city = my_form.text_input("Enter your city:")
pincode = my_form.number_input("Enter the Pincode")
state = my_form.text_input("Enter the State:")
qualification = my_form.checkbox('Bsc','Mca','Be')
Bsc = st.checkbox("Bsc")
Mca = st.checkbox("Mca")
Be = st.checkbox("Be")
selected_qualification =[]
if Bsc:
    selected_qualification.append("Bsc")
    if Mca:
        selected_qualification.append("Mca")
        if Be:
            selected_qualification.append("Be")

specialization = my_form.radio('specialization',('cs','IT','Computer Architecture','tel communication'))
password = my_form.text_input("Enter your Password:")
my_form.form_submit_button("Registered")

st.write("First_name",f_name)
st.write("Last_name",l_name)
st.write("Email",email)
st.write("Mobile number",mobile)
st.write("Gender",gender)
st.write("Age",age)
st.write("Date of birth",dob)
st.write("Address",address)
st.write("City",city)
st.write("State",state)
st.write("Qualification",selected_qualification)
st.write("Specialization",specialization)
st.write("password",password)